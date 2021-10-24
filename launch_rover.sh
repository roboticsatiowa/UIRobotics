#!/bin/bash

# Launch the robot
source ~/robotics_ws_git_test/devel/setup.bash 

echo "Launching application, please wait"
roslaunch rover rover_launch.launch 
