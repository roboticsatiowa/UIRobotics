# ROS Implementation of Main Rover Software

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

__________________________________________________________________________________________________________________________________________________________

### Terminal Commands:
- ls – list all files in current directory 
- cd - change directory 
  - cd dir1/dir2/dir3/etc to navigate forward through multiple directories 
  - cd .. /../etc to go backwards through directories 
  - cd takes you to home directory 
- mkdir -  
- sudo (command) - run administrator commands 
- whatis (command) - find function of different command 
- exit() - exit python to get back to (base) 

### Git Commands:
- git diff – check for differences 
- git pull – pull upstream changes and update your local repository 
- git push – push changes from your local repository to remote repository 
- git checkout  
  - -b  <name of branch> – make new branch 
  - <name of branch> - switch to <name> branch 
- git status – check which files have been changed 
- git add <file/folder name> - stage a file for commit 
- git commit -m “COMMENT” - commit changes to branch 
  - -a -m “COMMENT” - commit all changes 
  
### Extra resources: 
- https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html  
- https://www.techrepublic.com/article/16-terminal-commands-every-user-should-know/  

### Launching rover and base station 
- Connect antennas 
- ssh into Jetson 
```
  >>> ssh robotics@192.168.1.23
```
- Run rover launch file 
```
  >>> ./ launch_rover.sh.sh 
```
- Open base station terminal 
- Run base station launch file 
```
  >>> ./ launch_base.sh 
```
- Rover running :) 


### TODO:
- Should not launch non-necessary components of realsense ROS package
- Make a `requirements.txt` (similar file for ros packages?)
- Check if cameras are connected
