#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy

from std_msgs.msg import String
from nav_msgs.msg import Odometry

bool = False
arr={}
name=None
def callback1(data_qr):
    global bool
    global name
    # print(data_qr.data)
    if data_qr.data=="1": #박물관 전시품 적으면됌
        name=data_qr.data
        bool = True
    elif data_qr.data=="2":
        name=data_qr.data
        bool = True
    elif data_qr.data=="3":
        name=data_qr.data
        bool = True
    elif data_qr.data=="4":
        name=data_qr.data
        bool = True
    elif data_qr.data=="5":
        name=data_qr.data
        bool = True
    elif data_qr.data=="5 6 7 8":
        name=data_qr.data
        bool = True
    elif data_qr.data=="1 2 3 4":
        name=data_qr.data
        bool = True
    elif data_qr.data=="9 10 11 12":
        name=data_qr.data
        bool = True
    elif data_qr.data==None:
        name=False
        bool=False
        

def callback2(data_pos):
    global bool
    global arr
    global name
    pos_x=data_pos.pose.pose.position.x #현재위치 (x,y)
    pos_y=data_pos.pose.pose.position.y #현재위치 (x,y)
    qut_z=data_pos.pose.pose.orientation.z #현재각도 (z,w)
    qut_w=data_pos.pose.pose.orientation.w #현재각도 (z,w)

    
    if bool== True and name is not None:
        arr[name]=[pos_x,pos_y, qut_w,qut_z]
        name=None
        print(arr) 
        


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
        