#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
import rosnode
from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def api_root():
    callback('room')
    return 'Welcome'

@app.route('/navigate', methods=['POST'])
def api_articles():
    print(request.is_json)
    content = request.get_json()
    callback(content)
    print(content['text'])
    return 'json printed'

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
    print(msg)
	#rospy.loginfo('position: {}'.format(msg))

def main():
    if not rosnode.rosnode_ping('log_writer', 2):
	    rospy.init_node('log_writer')
    
    
if __name__ == '__main__':
    #main()
    app.run(debug=True)
