#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def main():
    twist = Twist()
    twist.linear.x = 2
    twist.linear.y = 2
    twist.linear.z = 2
    rospy.init_node('cmd_vel_publisher')
    rospy.loginfo("info")
    rospy.spin()

if __name__ == '__main__':
    main()