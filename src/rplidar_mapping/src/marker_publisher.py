#!/usr/bin/env python
topic = 'visualization_marker'
import rospy
from visualization_msgs.msg import Marker
import math

publisher = rospy.Publisher(topic, Marker, queue_size=10)

def init():
    rospy.init_node('marker_publisher')

    marker = Marker()
    marker.header.frame_id="map"
    marker.type = marker.SPHERE
    marker.action = marker.ADD
    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    marker.pose.orientation.w = 1.0
    marker.pose.position.x = 1
    marker.pose.position.y = 1 
    marker.pose.position.z = 1

    marker.id = 1

    publisher.publish(marker)

    rospy.sleep(0.01)
    print("posted")

if __name__ == "__main__":
    while not rospy.is_shutdown():
        init()  

