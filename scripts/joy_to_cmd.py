#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyToCmd:
    def __init__(self):
        self.cmd_vel = Twist()

    def joy_callback(self, data):
        self.cmd_vel.linear.x = data.axes[3]
        self.cmd_vel.angular.z = data.axes[2]

    def start_converter(self):
        rospy.init_node('joy_to_cmd')

        rospy.Subscriber("/joy", Joy, self.joy_callback)
        cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

        rater = rospy.Rate(20)
        while not rospy.is_shutdown():
            cmd_pub.publish(self.cmd_vel)
            rater.sleep()

if __name__ == "__main__":
    JoyToCmd().start_converter()
