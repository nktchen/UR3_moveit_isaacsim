#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from moveit_msgs.msg import CollisionObject
from shape_msgs.msg import SolidPrimitive
from geometry_msgs.msg import Pose

class FloorPublisher(Node):
    def __init__(self):
        super().__init__('floor_publisher')
        # топик для PlanningScene
        self.publisher = self.create_publisher(CollisionObject, 'collision_object', 10)
        self.publish_floor()

    def publish_floor(self):
        co = CollisionObject()
        co.id = "floor"
        co.header.frame_id = "world"

        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box.dimensions = [2.0, 2.0, 0.01]  # размеры пола: 5x5 метров, 1 см толщины

        pose = Pose()
        pose.position.z = -0.1 # центр пола чуть ниже 0

        co.primitives = [box]
        co.primitive_poses = [pose]
        co.operation = CollisionObject.ADD

        self.publisher.publish(co)
        self.get_logger().info("Published floor to PlanningScene")

def main(args=None):
    rclpy.init(args=args)
    node = FloorPublisher()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

