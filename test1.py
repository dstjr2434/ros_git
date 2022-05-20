#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy

from std_msgs.msg import String
from nav_msgs.msg import Odometry

bool = False

def callback1(data_qr):
    global bool
    if data_qr.data=="9 10 11 12":
        bool = True
    else:
        bool=False
        

def callback2(data_pos):
    global bool
    x=data_pos.pose.pose.position.x
    y=data_pos.pose.pose.position.y
    
    print(x)
    print(y)
    
    if bool== True:
        print(bool)
        print("성공2")
        
        


def subs():
    pass

if __name__=="__main__":
    try:
        rospy.init_node("check",anonymous=True)
        sub1=rospy.Subscriber("qr_topic",String,callback1)
        sub2=rospy.Subscriber("odom",Odometry,callback2)
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass
        