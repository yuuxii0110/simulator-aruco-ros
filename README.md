# simulator-aruco-ros

> This is a repository that contains aruco markers sdf files, aruco markers detections and aruco positioning system in **GAZEBO**. This project has been tested on UBUNTU 20.04 with ROS Noetic.
> This repository together with and (https://github.com/Junszz/espdrone.git) are specialized for the NTU EEE UAVIONICS DIP project.

# Aruco map
**1. Pulling from github.**
```
git pull https://github.com/yuuxii0110/simulator-aruco-ros.git
```

**2. Modified path to marker sdf files.**

Add the markers' folders to your gazebo model path. The markers folder are inside the directory: simulator-aruco-ros/aruco_markers. In this repository, markers id 0-10 are provided.

Alternatively, you may move all the folders into the ~/.gazebo/models path.

More markers with higher id can be generated on the website: 
https://damianofalcioni.github.io/js-aruco2/samples/marker-creator/marker-creator.html?dictionary=ARUCO_MIP_36h12

After markers in svg format has been generated, you may want to resize the the file and convert it into png format.
https://webkul.github.io/myscale/

**3. Check everything is done properly.**

Type the following command to check the models directories are correct.
```
gazebo <path_to_your_simulator-aruco-ros>/espdrone_aruco_bringup/environment/gazebo_world/aruco.world.world.
```
# Aruco detection and localization

**1. Install aruco library.**

Proceed to the website: https://sourceforge.net/projects/aruco/files/3.1.2/. Download and extract it.

**2. Customize path.**

In the simulator-aruco-ros/aruco_lib_integration/CMakelists.txt, on line 6, customize it to:
  SOURCE_DIR <path to your library>/aruco-3.1.12
  
**3. Customize the detection algorithm.**

The path, model_link_name ,model name and etc have to be customized for detection and localization. You may start from the launch file (simulator-aruco-ros/espdrone_aruco_bringup/launch/espdrone_aruco.launch) to get the insight of how everything is done.

If you are building your own aruco world, you have to "tell" your system where the aruco markers location in the gazebo.
To achieve this, you have to modified the file (simulator-aruco-ros/espdrone_aruco_bringup/environment/gazebo.yml)
You may use the python file (simulator-aruco-ros/espdrone_aruco_bringup/script/generate_coordinates.py) to generate marker corners' coordinates. The instructions are stated in the file.
