from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    pkg_path = get_package_share_directory('mohd_shan')
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')

    robot_description = ParameterValue(
        Command(['xacro ', xacro_file]),
        value_type=str
    )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description':robot_description}]
    )

    gazebo = ExecuteProcess(
        cmd=['gz','sim','-r','empty.sdf'],
        output='screen'
    )

    spawn = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic','robot_description',
            '-name','my_robot',
            '-z', '0.3'
        ],
        output='screen'
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn
    ])
