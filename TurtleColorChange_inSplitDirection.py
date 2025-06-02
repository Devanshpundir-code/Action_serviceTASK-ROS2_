import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from turtlesim.srv import SetPen
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose

class ChangeColor(Node):
    def __init__(self, node_name, *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False, enable_logger_service = False):
        super().__init__(node_name, context=context, cli_args=cli_args, namespace=namespace, use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides, enable_logger_service=enable_logger_service)
        self.client_ = self.create_client(SetPen, "/turtle1/set_pen")
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.sub_callback, 10)
        self.current_ = None

    def sub_callback(self, msg:Pose):
        if msg.x > 5.5 and self.current_ != 'right':
            self.get_logger().info("the turtle is on the right side of the page")
            self.current_ = 'right'
            self.set_pen_color(255, 0, 0) #red

        if msg.x < 5.5 and self.current_ != 'left':
            self.get_logger().info("the turtle is on the left side of the page")
            self.current_ = 'left'
            self.set_pen_color(0, 0 ,0) #white

    def set_pen_color(self, R, G, B):
        req = SetPen.Request()
        req.r = R
        req.g = G
        req.b = B

        req.width = 2
        req.off = 0
        self.client_.call_async(req)


def main(args=None):
    rclpy.init(args=args)
    node = ChangeColor("change_color_node")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        




        
