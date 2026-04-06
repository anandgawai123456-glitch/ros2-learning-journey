# 🚀 ROS2 Learning Journey – Anand Gawai

This repository documents my complete journey of learning **ROS 2 (Robot Operating System 2)** from basics to real-world robotics applications.

---

## 📌 About This Repository

This project includes hands-on implementation of:

* ROS2 Nodes (Python)
* Topics (Publisher & Subscriber)
* Services & Clients
* Custom Interfaces (Messages)
* Simulation using Gazebo
* Hardware Integration (ESP8266 + Ultrasonic Sensor)

---

## 🧠 Skills Demonstrated

* ROS2 package creation and management
* Writing publisher and subscriber nodes
* Creating and using ROS2 services
* Building custom `.msg` interfaces
* Debugging build and runtime errors
* Simulation using Gazebo
* Serial communication with hardware
* Integrating real-world sensor data into ROS2

---

## 📂 Project Structure

```
ros2_ws/
 ├── src/
 │   ├── my_robot_pkg/
 │   ├── my_robot_interfaces/
 │   └── dummy_robot_bringup/
 ├── build/
 ├── install/
 └── log/
```

---

## 🔧 Key Projects

### 1️⃣ Temperature Service Node

* Created a ROS2 service
* Returns temperature using `example_interfaces/srv/Trigger`

---

### 2️⃣ Custom Message (RobotStatus)

* Created custom `.msg` file
* Built interface package
* Used in ROS2 nodes

---

### 3️⃣ Gazebo Simulation – Simple Robotic Arm

* Created URDF model
* Spawned robot in Gazebo
* Learned simulation pipeline

---

### 4️⃣ Ultrasonic Sensor Integration (ESP8266)

* Read real-world distance data
* Sent data via Serial
* Published data into ROS2 topic `/distance`

---

## 🔌 Hardware Used

* ESP8266 (NodeMCU)
* Ultrasonic Sensor (HC-SR04)
* Jumper Wires
* Voltage Divider (for safe operation)

---

## ⚙️ How to Run

### Build Workspace

```
cd ~/ros2_ws
colcon build
source install/setup.bash
```

---

### Run Example Node

```
ros2 run my_robot_pkg publisher_node
```

---

### Run Ultrasonic Sensor Node

```
ros2 run my_robot_pkg ultrasonic_pub
ros2 topic echo /distance
```

---

### Launch Gazebo Simulation

```
ros2 launch my_robot_pkg simple_arm.launch.py
```

---

## 🚧 Challenges Faced

* CMake and package.xml errors
* Module import issues in Python
* Serial communication bugs
* Gazebo spawn issues
* Hardware voltage mismatch

---

## 💡 Learnings

* Real robotics requires debugging at every level
* Integration of hardware + software is critical
* Understanding ROS2 architecture deeply is important

---

## 🎯 Future Goals

* Implement obstacle avoidance robot
* Integrate ESP8266 via WiFi with ROS2
* Use TurtleSim with real sensor data
* Learn `ros2_control` for robot actuation
* Build full autonomous robotic system

---

## 📎 Author

**Anand Pradeep Gawai**
Electrical Engineer | Robotics Enthusiast

---

## ⭐ Conclusion

This repository represents my practical journey into robotics using ROS2, combining simulation and real-world hardware integration.

---

⭐ *Feel free to explore, fork, and contribute!*

