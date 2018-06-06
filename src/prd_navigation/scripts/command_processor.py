#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from prd_navigation.msg import command_msg
import json

def handler(data):
    print(data)
    try:
        destination = get_destination(data.value)
        result = movebase_client(destination)
        if result:
            print("Goal execution done!")
    except rospy.ROSInterruptException:
        print("Navigation test finished.")
        print("process finished")
    print(data)

def listener():
    print('started')
    rospy.init_node('command_processor', anonymous=True)
    rospy.Subscriber('alexa_command', command_msg, handler)
    rospy.spin()


def getGoal(x,y):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = -0.227663040161
    goal.target_pose.pose.position.y = 2.27461719513
    goal.target_pose.pose.orientation.w = 1.0
    return goal

def get_destination(tag):
    file = open('mapping.json', 'r')
    content = json.load(file)
    x = content['mappings'][0]['pose_x']
    y = content['mappings'][0]['pose_y']
    print(content['mappings'][0]['pose_x'] + content['mappings'][0]['pose_y'])
    return getGoal(x, y)

def movebase_client(room):

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    client.send_goal(room)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    #get_destination()
    listener()