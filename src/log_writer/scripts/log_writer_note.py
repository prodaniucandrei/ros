#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def callback(msg):
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y
	rospy.loginfo('position: {} {}'.format(x,y))

def main():
	rospy.init_node('log_writer')
	rospy.Subscriber("/odom", Odometry, callback)
	rospy.spin()

if __name__ == '__main__':
	main()