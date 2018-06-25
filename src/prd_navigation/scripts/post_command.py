#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from prd_navigation.msg import command_msg


def PostPose(room):
    print('start publish: '+room)
    rospy.init_node('post_command', disable_signals=True, anonymous=True)
    pub = rospy.Publisher('alexa_command', command_msg, queue_size=10)
    rate = rospy.Rate(10, reset=True)
    rate.sleep()
    command = command_msg()
    command.command_name = "nav"
    command.value = int(room)
    pub.publish(command)
    rate.sleep()
    print('published')
    #rospy.signal_shutdown("finished")

def PostAction(action):
    rospy.set_param('action',action)
    # print('start publish: ' + action)
    # rospy.init_node('post_action', disable_signals=True, anonymous=True)
    # pub = rospy.Publisher('alexa_action', command_msg, queue_size=10)
    # rate = rospy.Rate(10, reset=True)
    # rate.sleep()
    # command = command_msg()
    # command.command_name = "action"
    # command.action = action
    # pub.publish(command)
    # rate.sleep()
    # print('published')    