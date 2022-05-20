#! /usr/bin/env python
# -*- coding: utf-8 -*-


import rospy

from geometry_msgs.msg import PoseWithCovarianceStamped #amcl pose


def callback1(data):
    
    print(data.pose.pose.position)#x,y,z
    print(data.pose.pose.orientation)#x,y,z,w

if __name__=="__main__":
    try:
        rospy.init_node("check",anonymous=True)
        sub1=rospy.Subscriber("amcl_pose",PoseWithCovarianceStamped,callback1)
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass