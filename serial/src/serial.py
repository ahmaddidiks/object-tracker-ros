#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16 
#from .SerialClient import *
#import rosserial_arduino import SerialClient
#from serial import SerialException
from time import sleep

import sys

rospy.init_node("talker")

pub = rospy.Publisher('chatter', UInt16, queue_size=1)
rate = rospy.Rate(10)
#port_name = rospy.get_param('~port','/dev/ttyUSB0')
#baud = int(rospy.get_param('~baud', '57600'))


def kirim():
    x = 10
    rospy.loginfo("dikirim : %d",x)
    pub.publish(x)
    rate.sleep()


if __name__ == "__main__":
    while not rospy.is_shutdown():
        try:
            kirim()
        except rospy.ROSInterruptException:
            print("gagal")