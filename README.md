<img title="" src="./FemtomesLogo.png" alt="" data-align="center">

# ROS Wrapper for Femtomes Nano-D Reciver

There are packages for using Femtomes Reciver (Nano-D) with ROS.

This version supports Noetic distribution.

For running in Melodic environment please switch to the [melodic](https://github.com/DapengFeng/femtomes_ros_driver/tree/melodic). 

## Requirements

- Hardware
  
  - [Nano-D](http://www.femtomes.com/en/Nano.php?name=Nano)<img src="./Nano_D.png" title="" alt="" data-align="center">

- Software
  
  - [ROS Noetic on Ubuntu 20.04](http://wiki.ros.org/noetic/Installation/Ubuntu)  or [ROS Noetic or later on Windows 10](https://wiki.ros.org/Installation/Windows)
  
  - Python3.x

## Install from Sources

1. Create a [catkin](http://wiki.ros.org/catkin#Installing_catkin) workspace

*ubuntu*

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
```

*windows*

```batch
mkdir c:\catkin_ws\src
cd c:\catkin_ws\src
```

2. Clone the Femtomes  ROS Driver from [here](https://github.com/DapengFeng/femtomes_ros_driver) into 'catkin_ws/src/' and make

```bash
git clone https://github.com/DapengFeng/femtomes_ros_driver.git
cd ..
catkin_make
```

## Usage Instructions

### Start the femtomes node in ROS:

```bash
roslaunch femtomes_ros_driver femtomes_rtk.launch
```

This will stream femtomes reciver and publish on the appropriate ROS topic.

### Published Topics

- /femtomes/bestxyz ([femtomes_msgs/BESTXYZ](https://raw.githubusercontent.com/DapengFeng/femtomes_ros_driver/main/msg/FemtomesBESTXYZ.msg))

- /femtomes/heading ([femtomes_msgs/HEADING](https://raw.githubusercontent.com/DapengFeng/femtomes_ros_driver/main/msg/FemtomesHEADING.msg))

- /femtomes/odom ([nav_msgs/Odometry](http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html))


