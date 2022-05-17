#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import rospy
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionResult

# coord_list = [[0, 0, 0, 1], [3, 0, -0.7, 0.7], [3, -1.5, 1, 0], [2, -3, -0.7, 0.7], [3.3, -3, 0, 1], [3.3, -5, -0.7, 0.7], [1, -5, 1, 0], [0, -2, 0.7, -0.7]]
coord_list = [[0, 0, 0, 1], [3, 0, -0.7, 0.7], [3, -1.5, 1, 0], [0, -1.5, 0.7, 0.7]]

def callback(data):
    rospy.init_node('slam_nav', anonymous=True)
    pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)
    nav_msg = PoseStamped()
    nav_msg.header.frame_id = 'map'
    
    
    if data.status.status == 3:
        global cnt
        cnt += 1
        if cnt == len(coord_list):
            cnt = 0
        print('도착 ㅋㅋ루삥뽕')
        nav_msg.pose.position.x = coord_list[cnt][0]
        nav_msg.pose.position.y = coord_list[cnt][1]

        nav_msg.pose.orientation.z = coord_list[cnt][2]
        nav_msg.pose.orientation.w = coord_list[cnt][3]
        print('다음 ㄱㄱ씽!!!')
        pub.publish(nav_msg)
        
    

def listener():
    global cnt
    cnt = 0
    rospy.init_node('slam_nav', anonymous=True)
    pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)
    rospy.Subscriber('move_base/result', MoveBaseActionResult, callback)
    nav_msg = PoseStamped()
    
    nav_msg.pose.position.x = coord_list[cnt][0]
    nav_msg.pose.position.y = coord_list[cnt][1]
    nav_msg.pose.orientation.z = coord_list[cnt][2]
    nav_msg.pose.orientation.w = coord_list[cnt][3]
    
    print('초기 위치 0, 0으로 이동합니다.')
    pub.publish(nav_msg)
    
    rospy.spin()
    
if __name__ == '__main__':
    listener()