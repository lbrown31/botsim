import pybullet as p
import time
physicsClient = p.connect(p.GUI)
for i in range(1000):
    print(f'Iteration: {i+1}')
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()