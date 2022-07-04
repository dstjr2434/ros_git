#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# import rospy
# import math
# import actionlib
# from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
# from actionlib_msgs.msg import GoalStatus
# from geometry_msgs.msg import Pose, Point, Quaternion
# from tf.transformations import quaternion_from_euler

# '''
# -Takes position and orientation from launch file parameter
# -Uses action to send sequence of goal positions to robot
# '''

import rospy
import math
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Pose, Point, Quaternion
# from tf.transformations import quaternion_from_euler
import numpy as np
'''
-Takes position and orientation from launch file parameter
-Uses action to send sequence of goal positions to robot
'''
class MoveBaseSeq():
    def __init__(self):
        rospy.init_node('move_base_sequence')
        # get [x1,y1,z1,x2,y2,z2...etc] from launch parameter
        points_seq = rospy.get_param('move_base_seq/p_seq')
        print(points_seq)
        # get [yaw1,yaw2,yaw3] in degrees from launch parameter
        yaweulerangles_seq = rospy.get_param('move_base_seq/yea_seq')
        print(yaweulerangles_seq)
        # List of goal quaternions:
        quat_seq = list()
        # List of goal poses:
        self.pose_seq = list()
        self.goal_cnt = 0
        '''###########'''
        # Euler angle in our parameter to quartanian conversion
        for yawangle in yaweulerangles_seq:
            # Unpacking the quaternion tuple and passing it as arguments to Quaternion message constructor
            quat_seq.append(Quaternion(*(self.get_quaternion_from_euler(0, 0, yawangle*math.pi/180))))
            #quat_seq.append(Quaternion(*(quaternion_from_euler(0, 0, yawangle*math.pi/180, axes='sxyz'))))
        n = 3  # becuase in launch param we use [xn,yn,zn] format
        
        # Returns points in points_seq [[point1], [point2],...[pointn]]
        points = [points_seq[i:i+n] for i in range(0, len(points_seq), n)]
        rospy.loginfo(str(points))
        # for [x1,y1,z1] in [x1,y1,z1,x2,y2,z2...etc]
        for point in points:
            # use same n variable to cycle in quat_seq
            self.pose_seq.append(Pose(Point(*point), quat_seq[n-3]))
            n += 1
        # rospy.loginfo(str(self.pose_seq))
        # Create action client
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        rospy.loginfo("Waiting for move_base action server...")
        #wait = self.client.wait_for_server(rospy.Duration(5.0))
        wait = self.client.wait_for_server()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
            return
        rospy.loginfo("Connected to move base server")
        rospy.loginfo("Starting goals achievements ...")
        # MAIN MOVEMENT METHOD
        self.movebase_client()

    def get_quaternion_from_euler(self, roll, pitch, yaw):
      
        qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
        qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
        qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
 
        return [qx, qy, qz, qw]
    
    def active_cb(self):
        rospy.loginfo("Goal pose "+str(self.goal_cnt+1) +
                      " is now being processed by the Action Server...")
    def feedback_cb(self, feedback):
        #rospy.loginfo("Feedback for goal "+str(self.goal_cnt)+": "+str(feedback))
        rospy.loginfo("Feedback for goal pose " +
                      str(self.goal_cnt+1)+" received")
    def done_cb(self, status, result):
        self.goal_cnt += 1
        if status == 2:
            rospy.loginfo("Goal pose "+str(self.goal_cnt) +
                          " received a cancel request after it started executing, completed execution!")
        if status == 3:
            rospy.loginfo("Goal pose "+str(self.goal_cnt)+" reached")
            # if more goal left, keep going
            if self.goal_cnt < len(self.pose_seq):
                next_goal = MoveBaseGoal()  # MoveBaseGoal is action message type for move_base/goal
                next_goal.target_pose.header.frame_id = "map"
                next_goal.target_pose.header.stamp = rospy.Time.now()
                next_goal.target_pose.pose = self.pose_seq[self.goal_cnt]
                rospy.loginfo("Sending goal pose " +
                              str(self.goal_cnt+1)+" to Action Server")
                rospy.loginfo(str(self.pose_seq[self.goal_cnt]))
                # action client goal command
                self.client.send_goal(
                    next_goal, self.done_cb, self.active_cb, self.feedback_cb)
            # else shutdown
            else:
                rospy.loginfo("Final goal pose reached!")
                rospy.signal_shutdown("Final goal pose reached!")
                return
        if status == 4:
            rospy.loginfo("Goal pose "+str(self.goal_cnt) +
                          " was aborted by the Action Server")
            rospy.signal_shutdown(
                "Goal pose "+str(self.goal_cnt)+" aborted, shutting down!")
            return
        if status == 5:
            rospy.loginfo("Goal pose "+str(self.goal_cnt) +
                          " has been rejected by the Action Server")
            rospy.signal_shutdown(
                "Goal pose "+str(self.goal_cnt)+" rejected, shutting down!")
            return
        if status == 8:
            rospy.loginfo("Goal pose "+str(self.goal_cnt) +
                          " received a cancel request before it started executing, successfully cancelled!")
    def movebase_client(self):
        goal = MoveBaseGoal()  # MoveBaseGoal is action message type for move_base/goal
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = self.pose_seq[self.goal_cnt]
        rospy.loginfo("Sending goal pose " +
                      str(self.goal_cnt+1)+" to Action Server")
        rospy.loginfo(str(self.pose_seq[self.goal_cnt]))
        self.client.send_goal(goal, self.done_cb,
                              self.active_cb, self.feedback_cb)
        rospy.spin()
if __name__ == '__main__':
    try:
        MoveBaseSeq()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation finished.")
