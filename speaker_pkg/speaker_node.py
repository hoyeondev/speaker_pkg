import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os

class SpeakerNode(Node):
    def __init__(self):
        super().__init__('speaker_node')
        self.subscription = self.create_subscription(
            String,
            'speaker_command',
            self.command_callback,
            10
        )

    def command_callback(self, msg):

        if msg.data == "start_delivery":
            self.get_logger().info("배달 시작 음성 재생")
            os.system("aplay ~/sound/start_delivery.wav")

        if msg.data == "arrival":
            self.get_logger().info("arrival 음성 재생")
            os.system("aplay ~/sound/arrival.wav")

        if msg.data == "user_authentication":
            self.get_logger().info("user_authentication 재생")
            os.system("aplay ~/sound/user_authentication.wav")


        if msg.data == "finish_delivery":
            self.get_logger().info("finish_delivery 재생")
            os.system("aplay ~/sound/finish_delivery.wav")


def main(args=None):
    rclpy.init(args=args)
    node = SpeakerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
