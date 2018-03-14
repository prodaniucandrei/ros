#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def stopRobot():
    rospy.loginfo('stooop')

def callback(msg):
    rospy.loginfo("rangemax %s" %msg.range_max)
    rospy.loginfo(len(msg.ranges))
    rospy.loginfo(msg.ranges)
    rospy.sleep(10)
    if any(x>1.0 for x in msg.ranges):
        stopRobot()
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
    twist = Twist()
    twist.linear.x = 3.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)


if __name__ == '__main__':
    rospy.init_node('obstacle_demo')
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()