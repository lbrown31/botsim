import pyrosim.pyrosim as pyrosim
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

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    '''
    pyrosim.Send_Cube(name="Link0", pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name = "Link0_Link1", parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link1", pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name = "Link1_Link2", parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link2", pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name = "Link2_Link3", parent= "Link2" , child = "Link3" , type = "revolute", position = [0,.5,.5])
    pyrosim.Send_Cube(name="Link3", pos=[x, .5, 0], size=[length, width, height])
    '''
    pyrosim.Send_Cube(name = "Torso", pos = [1.5, 0, 1.5], size = [length, width, height])
    pyrosim.Send_Joint(name = "Torso_Backleg", parent= "Torso" , child = "Backleg" , type = "revolute", position = [1, 0, 1])
    pyrosim.Send_Cube(name = "Backleg", pos = [-.5, 0, -.5], size = [length, width, height])
    pyrosim.Send_Joint(name = "Torso_Frontleg", parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name = "Frontleg", pos = [.5, 0, -.5], size=[length, width, height])

    pyrosim.End()

Create_World()
Create_Robot()

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



