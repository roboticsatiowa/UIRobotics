# ROS Example (with GUI)

```
$ mkdir robotics_ws

$ cd robotics_ws

$ git clone -b gui-ros https://github.com/roboticsatiowa/UIRobotics.git .

$ catkin_make

$ bash ./launch_rover.sh
```

### Prerequisites:
- Install [realsense-ros wrapper](https://github.com/IntelRealSense/realsense-ros)
- In a separate terminal window run `roslaunch realsense2_camera rs_camera.launch`

### TODO:
- Incorporate realsense ROS package into main package
  - Everything should launch with `launch_rover.sh`
  - Should not launch non-necessary components of realsense ROS package
- Simplify PyQt structure (too many layouts and widgets?)
- Make a `requirements.txt`
- Write better instructions
