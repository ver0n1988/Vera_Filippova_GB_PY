class Road:

    _length: float
    _width: float

    def __init__(self, length: float = 0, width: float = 0) -> None:
        self._length = length
        self._width = width

    def calc(self, density: float, thickness: float) -> float:
        return self._length * self._width * density * thickness


if __name__ == "__main__":
    road = Road(length=20, width=5000)
    print(road.calc(25, 5))

    # or if we in module
    road = Road()
    road._length = 20
    road._width = 5000
    print(road.calc(density=25, thickness=5))