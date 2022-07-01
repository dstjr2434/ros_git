#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys, select, termios, tty,time
import rospy
import numpy as np
import time
from math import cos, sin
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


np.set_printoptions(precision=2)# np를 쓰는 모든 데이터형식을 소수점 2자리까지 나타냄

orbit = 0
laser_sensors = {'w': 0, 'nw': 0, 'n': 0, 'ne': 0, 'e': 0}
linear_vel = 0.2
angular_vel = 0.6
wall_distance = 0.5 #완전정면
wall_distance_forward = 0.60 #전방측면
wall_distance_side = 0.7 #측면

inf = float('inf')
left = -1
going_left = -2
right = 1
going_right = 2


def calculate_lasers_range(data):
    '''Dynamic range intervals'''
    global laser_sensors
    # print(1)
    #np.mean()->뒤에 들어오는 값들의 전체 평균을 더해줌, 만약 2차원배열형태로 들어와도 모두 1차원 배열처럼 계산해줌
    #np.mean(arr, axis=0)->2차원 배열로 들어오게된다면 열(세로 값들의 평균을 구함)
    #np.mean(arr, axis=1))->2차원 배열로 들어오게된다면 행(가로 값들의 평균을 구함)
    
    # np.setdiff1d() -> 차집합을 쓴것, 앞의 인자에서 뒤에 인자를 빼준다.
    laser_sensors['e'] = np.mean(data.ranges[525:535]) #동(딕셔너리형태로 값을 넣어줌)
    laser_sensors['ne'] = np.mean(data.ranges[615:645]) #북동(딕셔너리형태로 값을 넣어줌)
    laser_sensors['n'] = np.mean(data.ranges[:35] + data.ranges[-35:]) #북쪽(딕셔너리형태로 값을 넣어줌)
    laser_sensors['nw'] = np.mean(data.ranges[75:105]) #북서(딕셔너리형태로 값을 넣어줌)
    laser_sensors['w'] = np.mean(data.ranges[165:195]) #서(딕셔너리형태로 값을 넣어줌)
    # half_pi = np.pi / 2
    # initial_angle = 0
    # final_angle = 0
    # if data.angle_min < -half_pi:
    #     default_min_angle = half_pi / data.angle_increment
    #     robot_initial_angle = -data.angle_min / data.angle_increment
    #     initial_angle = robot_initial_angle - default_min_angle
    # if data.angle_max > np.pi / 2:
    #     default_max_angle = half_pi / data.angle_increment
    #     robot_final_angle = data.angle_max / data.angle_increment
    #     final_angle = robot_final_angle - default_max_angle

    # laser_interval = (len(data.ranges) - initial_angle - final_angle) / 5
    # half_laser_interval = laser_interval / 2

    # interval = [None] * 5
    # interval[0] = np.mean(data.ranges[int(initial_angle):int(laser_interval)])
    # for i in range(1, 5):
    #     dirty_values = data.ranges[int(
    #         initial_angle + i * laser_interval - half_laser_interval
    #     ):int(initial_angle + i * laser_interval + half_laser_interval) + 1]
    #     interval[i] = np.mean(np.nan_to_num(dirty_values))

    # laser_sensors['e'] = interval[0]
    # laser_sensors['ne'] = interval[1]
    # laser_sensors['n'] = interval[2]
    # laser_sensors['nw'] = interval[3]
    # laser_sensors['w'] = interval[4]


def log_info():
    '''Initial orbit state'''
    global orbit, laser_sensors
    orbit_values = {-2: 'Going Left', -1: 'Left', 0: 'Undefined', 1: 'Right', 2: 'Going Right'}
    rospy.loginfo("Orbit: %s, W : %s, NW: %s, N : %s, NE: %s, E : %s", orbit_values[orbit],
                  laser_sensors['w'], laser_sensors['nw'], laser_sensors['n'],
                  laser_sensors['ne'], laser_sensors['e'])


def create_velocity_message(turn_left, turn_right, forward):
    angular = 0
    linear = 0
    if (turn_left):
        angular += angular_vel
    if (turn_right):
        angular -= angular_vel
    if (forward):
        linear = linear_vel
    vel_msg = Twist()
    vel_msg.linear.x = linear
    vel_msg.angular.z = angular
    return vel_msg


def create_velocity_message1():
    # print("예외발생")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    twist = Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.0

    while pub.get_num_connections()<1:
        time.sleep(1)
    # print("실행 3333")
    pub.publish(twist)



def publish_velocity_message(vel_msg):
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    vel_pub.publish(vel_msg)
    # print(vel_msg) 

def laser_callback(data):
    global orbit, laser_sensors

    #전역변수에 있는 laser_sensors = {'w': 0, 'nw': 0, 'n': 0, 'ne': 0, 'e': 0}
    #값을 계속해서 갱신시켜주는 코드
    calculate_lasers_range(data)
    # print(a)
    # rospy.loginfo("Orbit: %s, W : %s, NW: %s, N : %s, NE: %s, E : %s")
    # 갱신되어있는 데이터값들을 보여주는 코드
    log_info()

    linear = 0
    angular = 0
    forward = False
    turn_left = False
    turn_right = False
    if (orbit == 0):
        if (laser_sensors['w'] < wall_distance_side):
            orbit = left
        elif (laser_sensors['e'] < wall_distance_side):
            orbit = right
        elif (laser_sensors['nw'] < wall_distance):
            orbit = going_left
            turn_right = True
        elif (laser_sensors['ne'] < wall_distance):
            orbit = going_right
            turn_left = True
        elif (laser_sensors['n'] < wall_distance_forward):
            orbit = going_left
            turn_right = True
        else:
            forward = True
    elif (orbit == going_left or orbit == going_right):
        if (laser_sensors['w'] < wall_distance_side):
            orbit = left
        elif (laser_sensors['e'] < wall_distance_side):
            orbit = right
        elif (orbit == going_left):
            turn_right = True
        elif (orbit == going_right):
            turn_left = True
    elif (orbit == left):
        if (laser_sensors['n'] > wall_distance_forward
                and (laser_sensors['w'] > wall_distance_side or laser_sensors['e'] > wall_distance_side)):
            forward = True
            
        if (laser_sensors['w'] <= wall_distance_side
                and laser_sensors['e'] <= wall_distance_side):
            turn_right = True
        elif (laser_sensors['nw'] <= wall_distance
            or laser_sensors['ne'] <= wall_distance):
            turn_right = True
        else:
            if (laser_sensors['ne'] < wall_distance
                    or laser_sensors['nw'] < wall_distance
                    or laser_sensors['n'] < wall_distance_forward):
                turn_right = True
            else:
                turn_left = True               
    elif (orbit == right):
        if (laser_sensors['n'] > wall_distance_forward
                and (laser_sensors['w'] > wall_distance_side
                    or laser_sensors['e'] > wall_distance_side)):
            forward = True


        if (laser_sensors['w'] <= wall_distance_side
                and laser_sensors['e'] <= wall_distance_side):
            turn_left = True
        elif (laser_sensors['nw'] <= wall_distance
            or laser_sensors['ne'] <= wall_distance):
            turn_left = True
        else:
            if (laser_sensors['ne'] < wall_distance
                    or laser_sensors['nw'] < wall_distance
                    or laser_sensors['n'] < wall_distance_forward):
                turn_left = True
            else:
                turn_right = True
    vel_msg = create_velocity_message(turn_left, turn_right, forward)

    publish_velocity_message(vel_msg)



def listeners():
    # rospy.init_node('avoid_wall_', anonymous=False)
    rospy.init_node('wall_follower', anonymous=False)
    rospy.Subscriber('/scan', LaserScan, laser_callback)
    rospy.on_shutdown(create_velocity_message1)
    rospy.spin()        



if __name__ == '__main__': # 메인함수일때 실행되게끔
    
    listeners()

    
    