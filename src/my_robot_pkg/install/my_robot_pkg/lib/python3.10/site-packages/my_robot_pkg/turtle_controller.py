import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.move_turtle)
        self.counter = 0

    def move_turtle(self):
        msg = Twist()

        if self.counter < 3:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 2.0

        self.publisher.publish(msg)
        self.counter += 1

        if self.counter > 6:
            self.counter = 0

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
