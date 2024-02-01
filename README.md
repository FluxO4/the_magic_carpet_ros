# Setup Guide

*get your wsl ip address
```bash
ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'
```

*run the python script
```bash
python3 main.py
```

*if you only want to build it instead of importing repositories again it, on subsequent runs, use
```bash
python3 main.py build
```

*change the endpoint in the src/Unity-Technologies/ROS-TCP-Endpoint/launch/endpoint.py file to your ip address


*source ros2 and the current workspace
```bash
source /opt/ros/humble/setup.bash
source install/setup.bash
```

*run the tcp connector for unity
```bash
ros2 launch ros_tcp_endpoint endpoint.py
```