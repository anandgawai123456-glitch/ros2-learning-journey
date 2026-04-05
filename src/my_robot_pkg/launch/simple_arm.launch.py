from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        )
    )

    spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'simple_arm',
            '-file', os.path.join(
                os.getcwd(), 'src/my_robot_pkg/urdf/simple_arm.urdf'
            )
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn
    ])
