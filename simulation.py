import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time, numpy
from robot import ROBOT
from world import WORLD

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT()
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

    def Run(self):
        for i in range(1000):
            #print(f'Iteration: {i+1}')
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            # c.back_sensor_vals[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
            # c.front_sensor_vals[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")

            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robotId,
            # jointName = b'Torso_Backleg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = backleg_motor_command_vector.item(i),
            # maxForce = 100)

            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robotId,
            # jointName = b'Torso_Frontleg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = frontleg_motor_command_vector.item(i),
            # maxForce = 100)

            time.sleep(1/2000)
    
    def __del__(self):
        p.disconnect()

