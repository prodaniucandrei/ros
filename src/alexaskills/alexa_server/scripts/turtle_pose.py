#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from prd_navigation.msg import command_msg

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
    # try:
    #     rospy.init_node('movebase_client_py', disable_signals=True)
    #     result = movebase_client(room)
    #     if result:
    #         rospy.loginfo("Goal execution done!")
    # except rospy.ROSInterruptException:
    #     rospy.loginfo("Navigation test finished.")
    #     rospy.signal_shutdown("process finished")

if __name__=='__main__':
    PostPose('1')
