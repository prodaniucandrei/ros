#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from prd_navigation.msg import command_msg
def handler(data):
    print(data)
    try:
        result = movebase_client(1)
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


def getGoal(room):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = -0.227663040161
    goal.target_pose.pose.position.y = 2.27461719513
    goal.target_pose.pose.orientation.w = 1.0
    return goal

def movebase_client(room):

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    client.send_goal(getGoal(room))
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    listener()