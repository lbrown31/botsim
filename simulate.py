import pybullet as p
import pybullet_data
import time, numpy, random
import pyrosim.pyrosim as pyrosim
import matplotlib.pylab as plt

backleg_amplitude = numpy.pi/8
backleg_frequency = 10
backleg_phaseOffset = numpy.pi/4

frontleg_amplitude = numpy.pi/4
frontleg_frequency = 10
frontleg_phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

x = numpy.linspace(0, 2 * numpy.pi, 1000)

targetAngles = numpy.sin(x)
targetAngles = (targetAngles) * (numpy.pi / 4)

backleg_motor_command_vector = backleg_amplitude * numpy.sin(backleg_frequency * x + backleg_phaseOffset)
frontleg_motor_command_vector = frontleg_amplitude * numpy.sin(frontleg_frequency * x + frontleg_phaseOffset)


angle_file_path = ("data/sine_wave_data.npy")
#numpy.save(angle_file_path, motor_command_vector)
#quit()

for i in range(1000):
    #print(f'Iteration: {i+1}')
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_Backleg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = backleg_motor_command_vector.item(i),
    maxForce = 100)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_Frontleg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = frontleg_motor_command_vector.item(i),
    maxForce = 100)


    time.sleep(1/240)

p.disconnect()
print(backLegSensorValues)

file_path = ("data/backLegValues.npy")
numpy.save(file_path, backLegSensorValues)
print(f"BackLeg sensor values saved to {file_path}")

frontLeg_file_path = ("data/frontLegValues.npy")
numpy.save(frontLeg_file_path, frontLegSensorValues)
print(f"FrontLeg sensor values saved to {frontLeg_file_path}")