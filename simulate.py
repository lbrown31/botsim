import pybullet as p
import pybullet_data
import time, numpy, random
import pyrosim.pyrosim as pyrosim
import matplotlib.pylab as plt
import constants as c
from simulation import SIMULATION

target_angles = numpy.sin(c.angles)
target_angles = (target_angles) * (numpy.pi / 4)
angle_file_path = ("data/sine_wave_data.npy")

simulation = SIMULATION()
simulation.Run()

