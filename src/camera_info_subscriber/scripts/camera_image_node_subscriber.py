#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image


def callback(image):
	rospy.loginfo(image.encoding)


def listener():
	rospy.init_node('camera_image_subscriber', anonymous = True)
	rospy.Subscriber('/camera/depth/image_raw', Image, callback)
	rospy.spin()


if __name__ == '__main__':
	listener()
