import pyrosim.pyrosim as pyrosim
import random
length = 1
width = 1
height = 1
x = 0
y = 0
z = height / 2

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x-2, y+2, z], size=[length, width, height])
    pyrosim.End()
'''
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name = "Torso", pos = [1.5, 0, 1.5], size = [length, width, height])
    pyrosim.Send_Joint(name = "Torso_Backleg", parent= "Torso" , child = "Backleg" , type = "revolute", position = [1, 0, 1])
    pyrosim.Send_Cube(name = "Backleg", pos = [-.5, 0, -.5], size = [length, width, height])
    pyrosim.Send_Joint(name = "Torso_Frontleg", parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name = "Frontleg", pos = [.5, 0, -.5], size=[length, width, height])

    pyrosim.End()
'''

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name = "Torso", pos = [1.5, 0, 1.5], size = [length, width, height])
    pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])
    pyrosim.Send_Cube(name = "BackLeg", pos = [-.5, 0, -.5], size = [length, width, height])
    pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name = "FrontLeg", pos = [.5, 0, -.5], size=[length, width, height])

    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    '''
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = -1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = -1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 0.0 )

    '''
    
    sensor_neurons = ["Torso", "BackLeg", "FrontLeg"]
    motor_neurons = ["Torso_BackLeg", "Torso_FrontLeg"]

    for sensor_name in sensor_neurons:
        pyrosim.Send_Sensor_Neuron(name=sensor_neurons.index(sensor_name), linkName=sensor_name)
    
    for motor_name in motor_neurons:
        pyrosim.Send_Motor_Neuron(name=motor_neurons.index(motor_name) + len(sensor_neurons), jointName=motor_name)
    
    for i, sensor_name in enumerate(sensor_neurons):
        for j, motor_name in enumerate(motor_neurons):
            weight = random.uniform(-1, 1) 
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j + len(sensor_neurons), weight=weight)
    
    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()


'''
for row in range(5):
    for col in range(5):
        # Calculate the position for the current tower
        newx = col * length
        newy = row * width
        newz = height / 2
        newlength = length
        newwidth = width
        newheight = height
        for _ in range(10):
            
            pyrosim.Send_Cube(name="Box", pos=[newx, newy, newz], size=[newlength, newwidth, newheight])
            newlength *= 0.9
            newwidth *= 0.9
            newheight *= 0.9
            newz += newheight
'''



