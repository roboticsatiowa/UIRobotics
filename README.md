# ROS Implementation of Main Rover Software

### Install and Run:

```
# create dir and clone repo
$ mkdir robotics_ws
$ cd robotics_ws
$ git clone https://github.com/roboticsatiowa/UIRobotics.git .

# build
$ catkin_make

# run
$ bash ./launch_rover.sh
```

_Note_ : Currently `launch_rover.sh` only launches (1) the sample GUI with realsense camera and usb camera feeds and (2) a dummy controller for testing. All other nodes can be manually launched.

### Prerequisites:
- Install [realsense2-ros](https://github.com/IntelRealSense/realsense-ros) package: `sudo apt-get install ros-melodic-realsense2-camera`

- Install [video-stream-opencv](https://github.com/ros-drivers/video_stream_opencv) package: `sudo apt-get install ros-melodic-video-stream-opencv`


### TODO:
- Should not launch non-necessary components of realsense ROS package
- Make a `requirements.txt` (similar file for ros packages?)
- Check if cameras are connected
