#!/usr/bin/env python
from post_command import PostPose, PostAction
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

@app.route('/actions/<action>', methods=['POST'])
def actions(action):
    rospy.loginfo(action)
    PostAction(action)
    return 'actions'

@app.route('/interactions', methods=['GET'])
def interactions():
    return 'interactions'

def callback(msg):
	rospy.loginfo('position: {}'.format(msg))

if __name__ == '__main__':
    app.run(debug=False)

