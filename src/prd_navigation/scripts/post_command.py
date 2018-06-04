#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from prd_navigation.msg import command_msg


def PostPose(room):
    print('start publish: '+room)
    rospy.init_node('post_command', disable_signals=True)
    pub = rospy.Publisher('alexa_command', command_msg, queue_size=10)
    rate = rospy.Rate(10)
    rate.sleep()
    command = command_msg()
    command.command_name = "nav"
    command.value = int(room)
    pub.publish(command)
    print('published')
    rospy.sleep(1)
    print('after sleep')
    rospy.signal_shutdown("finished")