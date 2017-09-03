class Lens:
    _f = None
    _focal_length = None

    def __init__(self, f, focal_length):
        self._f = f
        self._focal_length = focal_length

    @property
    def f(self):
        return self._f

    @property
    def focal_length(self):
        return self._focal_length
