#!/usr/bin/env python
from turtle_navigation import navigate_forward
from turtle_pose import PostPose
from geometry_msgs.msg import Twist
import rospy
from nav_msgs.msg import Odometry
import rosnode
from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def api_root():
    callback('room')
    return 'Welcome'

@app.route('/navigate/<room>', methods=['POST'])
def navigate(room):
    PostPose(room)
    return 'command executed'

@app.route('/querylocations', methods=['GET'])
def querylocations():
    return 'You are reading ' 

@app.route('/actions', methods=['POST'])
def actions():
    return 'actions'

@app.route('/interactions', methods=['GET'])
def interactions():
    return 'interactions'

def callback(msg):
	rospy.loginfo('position: {}'.format(msg))

def main():
    if not rosnode.rosnode_ping('log_writer', 2):
	    rospy.init_node('log_writer')

if __name__ == '__main__':
    #main()
    app.run(debug=True)

