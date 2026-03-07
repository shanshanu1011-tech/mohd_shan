from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():

    pkg_share = FindPackageShare(package='mohd_shan').find('mohd_shan')

    urdf_file = os.path.join(pkg_share, 'description', 'robot.urdf.xacro')

    robot_description = Command(['xacro ', urdf_file])

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # Node(
        #     package='joint_state_publisher',
        #     executable='joint_state_publisher',
        #     output='screen'
        # ),

        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        )
    ])
