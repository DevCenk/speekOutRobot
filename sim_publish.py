#!/usr/bin/python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('cmd', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = raw_input("Enter left or right: ")
        output_str = msg
        pub.publish(output_str)
        #rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
