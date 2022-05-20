#! /usr/bin/env python

import cv2
import pyzbar.pyzbar as pyzbar

import rospy
from std_msgs.msg import String

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


rospy.init_node('qr_node', anonymous=True)
pub = rospy.Publisher('qr_topic', String, queue_size=1)
# pub_img = rospy.Publisher('qr_image', Image, queue_size=1)
qr_msg = String()
bridge = CvBridge()


rate = rospy.Rate(5)

while not rospy.is_shutdown():
    retval, frame = cap.read()
    for code in pyzbar.decode(frame):
        detected_code = code.data.decode('utf-8')
        qr_msg.data = detected_code
        
        if qr_msg.data:
            # image_msg = bridge.cv2_to_imgmsg(frame,"bgr8")
            # pub_img.publish(image_msg)
            pub.publish(qr_msg)
            # print(qr_msg.data)
            rate.sleep()
        else:
            qr_msg=None
            pub.publish(qr_msg)
            rate.sleep()

    cv2.waitKey(1)
