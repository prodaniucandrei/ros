#!/usr/bin/env python

import rospy

def commandserver():
    rospy.init_node('command_server')
    s = rospy.Service('get_command', )

if __name__ == "__main__":
    commandserver()