# UR3_moveit_isaacsim
Use Moveit motion planning for UR3 in Isaac Sim.
# how to run it
1. navigate to your src directory in your moveit workspace (if you don't have one, then refer to the [moveit docs](https://www.genome.gov/](https://moveit.picknik.ai/main/doc/tutorials/getting_started/getting_started.html))
```bash
cd ~/ws_moveit/src
```

2. copy this repo
```bash
git clone https://github.com/nktchen/UR3_moveit_isaacsim.git ur3_moveit_config
```

3. build
```bash
cd ./../
colcon build --packages-select ur3_moveit_config
```

4. source the workspace
```bash
source ./install/setup.bash
```

5. run moveit
```bash
ros2 launch ur3_moveit_config demo.launch.py
```

6. run IsaacSim and open scene 
```
File -> Open -> path_to_your_moveit_workspace/src/ur3_moveit_config/omg.usd
```
and run the simulation
