# ROS Implementation of Main Rover Software

### TODO (Updated: 02/03/22):

- [ ] Verify you are in `gui-basics` branch (hint: use `$ git branch`). All changes you make should be in this branch. Once this task is finished it will be merged to `main`
- [ ] Follow run instructions below (use `launch_gui.sh` script) to verify current GUI functionality with ROS. Keep in mind that the USB camera will not work unless plugged into the correct port
- [ ] Read `src/rover/src/gui.py` and `src/rover/src/dummy_control.py` to understand how current GUI works
- [ ] _Optional_: Read `src/rover/launch/gui_launch.launch` and `launch_gui.sh` to understand how the GUI is launched (you should not have to change anything here
- [ ] Modify `src/rover/src/gui.py` to include all components of the new GUI (gps, timer, basic buttons, etc.) without ROS
- [ ] Create map (on paper) of ROS input/output topics for the GUI. Consider how multiple topics should/shouldn't be bundled
- [ ] Implement ROS sub/pubs with above's topics
- [ ] Code review with Will and Kyle
- [ ] Merge to `main`
- [ ] Celebrate with a beer

### Install and Run:

```
# create dir and clone repo
$ mkdir robotics_ws
$ cd robotics_ws
$ git clone https://github.com/roboticsatiowa/UIRobotics.git .

# build
$ catkin_make

# run drive wheels
$ bash ./launch_rover.sh

# run gui
$ bash ./launch_gui.sh
```

_Note_ : Currently `launch_gui.sh` only launches (1) the sample GUI with realsense camera and usb camera feeds and (2) a dummy controller for testing. All other nodes can be manually launched.

### Prerequisites:
- Install [realsense2-ros](https://github.com/IntelRealSense/realsense-ros) package: `sudo apt-get install ros-melodic-realsense2-camera`

- Install [video-stream-opencv](https://github.com/ros-drivers/video_stream_opencv) package: `sudo apt-get install ros-melodic-video-stream-opencv`


### TODO:
- Should not launch non-necessary components of realsense ROS package
- Make a `requirements.txt` (similar file for ros packages?)
- Check if cameras are connected
