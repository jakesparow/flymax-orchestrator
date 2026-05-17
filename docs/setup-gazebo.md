# Setup: Gazebo Harmonic + ROS 2 Humble (Phase 1)

> Required for `flymax fly --backend gazebo`. Skip this if you only want the `dryrun` backend.

## Why this combination

- **Gazebo Harmonic** — Bitcraze recommends it for Crazyflie sim as of 2026.
- **ROS 2 Humble** — current LTS, matches Crazyswarm2 mainline.
- **crazyflie_simulation** — Bitcraze's reference sim package.

## On Windows

Run all of this inside **WSL2 Ubuntu 22.04**. Native Windows ROS 2 + Gazebo is a road of pain.

```bash
# 1. Install WSL2 + Ubuntu 22.04 (if you haven't already)
wsl --install -d Ubuntu-22.04
# (open the Ubuntu shell from Start menu after install)

# 2. Inside Ubuntu — system update
sudo apt update && sudo apt upgrade -y

# 3. Install ROS 2 Humble (desktop, includes rviz2)
# (full guide: https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
sudo apt install -y software-properties-common curl gnupg lsb-release
sudo add-apt-repository universe
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
  http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
  | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install -y ros-humble-desktop ros-dev-tools

# 4. Source ROS 2 in every new shell
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

# 5. Install Gazebo Harmonic (Ignition successor)
sudo apt install -y ros-humble-ros-gz

# 6. Install crazyflie_simulation
mkdir -p ~/cf_ws/src && cd ~/cf_ws/src
git clone https://github.com/bitcraze/crazyflie-simulation.git
cd ~/cf_ws
colcon build --symlink-install
echo "source ~/cf_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Smoke test (no FlyMax yet)

```bash
# In one terminal — launch sim
ros2 launch crazyflie_simulation gz.launch.py

# In another terminal — verify ROS 2 is seeing the drone
ros2 topic list | grep crazyflie
```

You should see topics like `/crazyflie/cmd_vel`, `/crazyflie/odom`. If yes, ROS 2 is healthy.

## Wire FlyMax to the sim

(Phase 1 work — the Gazebo backend in this repo currently raises `NotImplementedError`.)

The backend will subscribe to the simulated Crazyflie's odom topic and publish setpoints on `/cmd_vel` for each waypoint. The Mission JSON stays unchanged — only the backend swap differs.

## On Linux / macOS native

Same steps, no WSL2. macOS Gazebo support is rough as of 2026 — consider running Gazebo in a Linux VM or Docker container.

## Hardware check

These specs let Gazebo run usefully:

- **Min:** quad-core x86_64 CPU, 8 GB RAM, GPU optional. Single drone, simple scene.
- **Comfortable:** 8-core CPU, 16 GB RAM, NVIDIA GPU with current drivers. Multi-drone, ROS 2 + rviz2.
- **Sriram's current laptop** — passes "min." Multi-drone scenes will be slow. Home server upgrade ([[embedded_home_lab_humanoid_2026_05_17]] in the brain) lifts this dramatically and re-opens Isaac Sim as the long-term simulator.
