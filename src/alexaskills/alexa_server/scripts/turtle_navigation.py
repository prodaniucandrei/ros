#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 
from std_msgs.msg import String

def navigate_forward(distance):
    print('aici')
    rospy.init_node('navigaterobot', disable_signals=True)
    msg = Twist()
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist,queue_size=10)
    msg.linear.x = float(distance)
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0
    rate = rospy.Rate(0.5)
    print('1')
    rate.sleep()
    print('2')
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()
        rospy.signal_shutdown('process finished')
    print('published')
    msg.linear.x = 0
    msg.linear.y = 0
    pub.publish(msg)
    #rospy.signal_shutdown('process finished')

if __name__ == '__main__':
    navigate_forward(10)