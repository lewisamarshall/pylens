from math import sqrt


class Sensor:
    _pixels = tuple()
    _size = tuple()

    def __init__(self, pixels, size):
        self._pixels = tuple(pixels)
        self._size = tuple(size)

    def __str__(self):
        lines = []
        lines.append('Sensor:')
        lines.append('pixels: {}'.format(self.pixels))
        lines.append('size: {}'.format(self.size))
        lines.append('pixel_size: {}'.format(self.pixel_size()))
        return '\n'.join(lines)

    @property
    def pixels(self):
       return self._pixels

    @property
    def size(self):
        return self._size

    def pixel_size(self):
        x = self.size[0]/self.pixels[0]
        y = self.size[1]/self.pixels[1]
        return sqrt(x**2+y**2)
