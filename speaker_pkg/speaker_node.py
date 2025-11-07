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
        self.last_command = None  # 마지막으로 재생한 명령 저장

    def command_callback(self, msg):
        # 같은 명령이 다시 들어오면 무시
        if msg.data == self.last_command:
            self.get_logger().info(f"중복 명령 '{msg.data}' 무시")
            return

        self.last_command = msg.data  # 현재 명령 저장

        if msg.data == "start_delivery":
            self.get_logger().info("배달 시작 음성 재생")
            os.system("aplay ~/sound/start_delivery.wav")

def main(args=None):
    rclpy.init(args=args)
    node = SpeakerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
