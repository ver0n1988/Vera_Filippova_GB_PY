import time
import enum


class Colour(enum.Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2


class TrafficLight:
    __colour: Colour
    __move: int = 1

    def __init__(self, colour: Colour) -> None:
        self.__colour = colour

    def running(self, green_t=7, red_t=7, yellow_t=2):

        for _ in range(10):  # while True:
            if self.__colour == Colour.RED:
                print(self.__colour.name)
                time.sleep(red_t)
            elif self.__colour == Colour.YELLOW:
                print(self.__colour.name)
                time.sleep(yellow_t)
            elif self.__colour == Colour.GREEN:
                print(self.__colour.name)
                time.sleep(green_t)

            if self.__colour.value == 2:
                self.__move = -1
            elif self.__colour.value == 0:
                self.__move = 1

            self.__colour = Colour(self.__colour.value + self.__move)


if __name__ == "__main__":
    traffic = TrafficLight(Colour.GREEN)
    traffic.running()