#!/bin/bash

# Launch the robot
source ~/robotics_ws/devel/setup.bash

echo "Launching application, please wait"
roslaunch rover rover_launch.launch 
