import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute #here i imported service type
from turtlesim.msg import Pose
import random


class RandomPosition(Node):
    def __init__(self, node_name, *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False, enable_logger_service = False):
        super().__init__(node_name, context=context, cli_args=cli_args, namespace=namespace, use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides, enable_logger_service=enable_logger_service)
        self.subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.random_callback, 10)
        self.client_ = self.create_client(TeleportAbsolute, "/turtle1/teleport_absolute")
        self.get_logger().info("the random position maker has been started")


    def random_callback(self, msg:Pose):
        Random_x = random.uniform(1.0,10.0)
        Random_y = random.uniform(1.0,10.0)

        self.get_logger().info("random location has beenn assigned")
        self.value_place_callback(Random_x, Random_y)

    def value_place_callback(self, X, Y):
        req = TeleportAbsolute.Request()
        req.x = X
        req.y = Y

        self.client_.call_async(req)


def main(args=None):
    rclpy.init(args=args)
    node = RandomPosition("random_position_node")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        
