import rospy
import random
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():

    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(1) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['collar_joint', 'link1_joint', 'link2_joint', 'link3_joint', 'brush_joint']
    hello_str.position = [0,0,0,0,0]
    pub.publish(hello_str)
    rate.sleep()

    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(1) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['collar_joint', 'link1_joint', 'link2_joint', 'link3_joint', 'brush_joint']
    hello_str.position = [0,0,0,1.57,3.14]
    pub.publish(hello_str)
    rate.sleep()

    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(1) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['collar_joint', 'link1_joint', 'link2_joint', 'link3_joint', 'brush_joint']
    hello_str.position = [0,0,-1.57,1.57,3.14]
    pub.publish(hello_str)
    rate.sleep()

    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(1) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['collar_joint', 'link1_joint', 'link2_joint', 'link3_joint', 'brush_joint']
    hello_str.position = [0,1,-1.57,1.57,3.14]
    pub.publish(hello_str)
    rate.sleep()

    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(1) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['collar_joint', 'link1_joint', 'link2_joint', 'link3_joint', 'brush_joint']
    hello_str.position = [1,0,-1.57,1.57,3.14]
    pub.publish(hello_str)
    rate.sleep()

    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(1) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['collar_joint', 'link1_joint', 'link2_joint', 'link3_joint', 'brush_joint']
    hello_str.position = [-1,-0.57,-1.57,1.57,3.14]
    pub.publish(hello_str)
    rate.sleep()

    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(1) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['collar_joint', 'link1_joint', 'link2_joint', 'link3_joint', 'brush_joint']
    hello_str.position = [0,0,0,0,0]
    pub.publish(hello_str)
    rate.sleep()
    
    while not rospy.is_shutdown():
      hello_str.header.stamp = rospy.Time.now()
      rospy.loginfo(hello_str)
      pub.publish(hello_str)
      rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
