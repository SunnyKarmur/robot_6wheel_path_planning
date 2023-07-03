import rospy
from geometry_msgs.msg import Twist
rospy.init_node('move_robot_node')
pub = rospy.Publisher('/effort_robot',Twist)
rate = rospy.Rate(2)
move = Twist()
move.linear.x = 0.5

while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()
