#!/usr/bin/env python

from geometry_msgs.msg import Twist
from math import radians
from prd_navigation.msg import command_msg
import rospy

class BotMotion():
    def __init__(self):
        rospy.init_node('botmotion', anonymous=True)
        rospy.on_shutdown(self.shutdown)

        self.execute = True

        self.command = Twist()

        self.cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(5)

        self.move_forward = Twist()
        self.move_forward.linear.x = 0.2

        self.turn_left = Twist()
        self.turn_left.angular.z = radians(45)

        self.turn_right = Twist()
        self.turn_right.angular.z = -radians(45)

        self.move_back = Twist()
        self.move_back.linear.x = -0.2

        self.stop = Twist()

    def shutdown(self):
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

    def Post_Cmd(self):
        self.execute = True
        while not rospy.is_shutdown():
            command = self.GetCommand()
            #print(command)
            if self.execute:
                self.cmd_vel.publish(command)
            self.rate.sleep()
            if command == self.stop:
                self.execute = False

    def GetCommand(self):
        action = ' '
        if rospy.has_param('action'):
            action = rospy.get_param('action')
        #print(action)
        if action == 'forward':
            self.execute = True
            return self.move_forward
        elif action == 'back':
            self.execute = True
            return self.move_back
        elif action == 'right':
            self.execute = True
            return self.turn_right
        elif action == 'left':
            self.execute = True
            return self.turn_left
        elif action == 'faster':
            self.execute = True
            self.move_forward.linear.x = self.move_forward.linear.x + 0.2
            return self.move_forward
        elif action == 'slower':
            self.execute = True
            self.move_back.linear.x = self.move_back.linear.x - 0.2
            return self.move_back
        else:
            return self.stop


    def ChangeAction(self, data):
        self.execute = False
        print(data)
        self.action = data.action
        self.Post_Cmd()

def listener():
    print('started')
    bot = BotMotion()
    bot.Post_Cmd()
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
        
    except Exception as ex:
        rospy.loginfo(ex.message)