import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxs.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = height / 2
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

pyrosim.End()

