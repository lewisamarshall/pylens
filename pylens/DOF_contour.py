from matplotlib import pyplot as plot
import numpy as np
from .Camera import Camera
from .Lens import Lens
from .Sensor import Sensor

sensor = Sensor(pixels=[4627, 3479],
                size=[18e-3, 13.5e-3])

print('something')
print(sensor)

lens = Lens(f=1.7,
            focal_length=25e-3)

camera = Camera(lens=lens, sensor=sensor)

print('Hyperfocal: {}'.format(camera.hyperfocal()))


distances = np.logspace(-1, 2)
apetures = np.linspace(lens.f, lens.f*10)

dof = np.zeros((len(distances), len(apetures)))

for idx, distance in enumerate(distances):
    for idx2, apeture in enumerate(apetures):
        dof[idx, idx2] = camera.depth_of_field(distance, apeture)


plot.loglog()
cp = plot.contour(distances, apetures, np.log10(dof))
plot.clabel(cp, inline=True,
           fontsize=10)
plot.xlabel('distance (m)')
plot.ylabel('F-number')
plot.show()
