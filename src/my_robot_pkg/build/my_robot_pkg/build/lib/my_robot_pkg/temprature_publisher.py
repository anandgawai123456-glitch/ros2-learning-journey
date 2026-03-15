import rclpy
from rclpy.node import node 
from std_msgs.msg import string

class TempraturePublisher(node):
     
   def __init_(self):
          super().__init__('tempraturepublisher')
           
          self.publisher_= self.create_publisher(string,"temprature", 10)

          self.timer = self.create_timer(1,0, self.publish_temprature)

def publish_temprature(self):
    msg = string()
    msg.data = "temprature: 45c"
 
    self,publisher_.publish(msg)
 
    self.get_logger().info(msg.data)
main(args=None):

rcply.init(args=args)

node = TempraturePublisher()

rcply.spin(node)

node.destroy_node()
fcply.shutdown()


__name__=='__main__':
main()
