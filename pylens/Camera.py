import warnings

class Camera:
    _lens = None
    _sensor = None

    def __init__(self, lens, sensor):
        self._lens = lens
        self._sensor = sensor

    @property
    def lens(self):
        return self._lens

    @property
    def sensor(self):
        return self._sensor

    def depth_of_focus(self):
        pass

    def hyperfocal(self, f=None):
        if f is None:
            f = self.lens.f
        elif f < self.lens.f:
            warnings.warn('Calculating f number below lens minimum.')
        H = self.lens.focal_length + self.lens.focal_length**2/f/self.sensor.pixel_size()
        return H

    def depth_of_field(self, distance, f=None):
        if f is None:
            f = self.lens.f
        elif f < self.lens.f:
            warnings.warn('Calculating f number below lens minimum.')
        H = self.hyperfocal(f)
        DOF = 2 * H * distance**2
        DOF /= H**2 - distance**2
        return DOF
