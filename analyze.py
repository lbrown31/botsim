import numpy
import matplotlib.pyplot as plt

#file_path = 'data/backLegValues.npy'
#frontLeg_file_path = ("data/frontLegValues.npy")
angle_file_path = ("data/sine_wave_data.npy")

#backLegValues = numpy.load(file_path)
#frontLegValues = numpy.load(frontLeg_file_path)
targetAngles = numpy.load(angle_file_path)

#plt.plot(backLegValues, label='BackLeg Sensor', linewidth=4)
#plt.plot(frontLegValues, label='FrontLeg Sensor')
plt.plot(targetAngles, label='Target Angle')
plt.legend()

plt.show()