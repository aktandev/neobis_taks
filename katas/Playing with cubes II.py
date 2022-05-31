class Cube(object):
    def __init__(self, _side=0):
        self._side = _side

    def get_side(self):
        if self._side < 0:
            return abs(self._side)
        return self._side


    def set_side(self, new_side):
        self._side = new_side


c = Cube(-10)
print(c.get_side())
c = Cube()
print(c.get_side())