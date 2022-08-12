#!/bin/bash

# Launch the robot
source ./devel/setup.bash

# export ROS_MASTER_URI=http://192.168.1.20:11311
# export ROS_IP=192.168.1.25

echo "Launching application, please wait"
roslaunch rover base_launch.launch
