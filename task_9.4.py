from enum import Enum


class TURN(Enum):
    LEFT = 0
    RIGHT = 1


class Car:
    speed: float
    _colour: str  # or use colour lib
    _name: str
    _is_police: bool = False

    def __init__(self, colour, name) -> None:
        self._colour = colour
        self._name = name

    def go(self) -> None:
        print(f"{self._name} is start")

    def stop(self) -> None:
        print(f"{self._name} is stop")

    def turn(self, turn_side: TURN) -> None:
        print(f"{self._name} is turn to {turn_side.name}")

    def show_speed(self) -> float:
        return self.speed


class TownCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)

    def show_speed(self) -> float:

        spd = super().show_speed()

        if spd > 40:
            print("Overspeed (40)")

        return spd


class SportCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)


class WorkCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)

    def show_speed(self) -> float:
        spd = super().show_speed()

        if spd > 60:
            print("Overspeed (60)")

        return spd


class PoliceCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)
        self._is_police = True


if __name__ == "__main__":
    abstract_car = Car("Transparent", "SomeCar")
    town_car = TownCar("Black", "TownCar")
    work_car = WorkCar("Green", "WorkCar")
    police_car = PoliceCar("DarkBlue", "PoliceCar")

    abstract_car.speed = -100 # =)
    town_car.speed = 120
    work_car.speed = 160
    police_car.speed = 175

    for some in [abstract_car, town_car, work_car, police_car]:
        print(f"{some.__class__}._name = {some._name}")
        print(f"{some.__class__}._colour = {some._colour}")
        print(f"{some.__class__}._is_police = {some._is_police}")

        print(f"{some.__class__}.go() => ", end="")
        some.go()

        print(f"{some.__class__}.stop() => ", end="")
        some.stop()

        print(f"{some.__class__}.turn(TURN.RIGHT) => ", end="")
        some.turn(TURN.RIGHT)

        print(f"{some.__class__}.turn(TURN.LEFT) => ", end="")
        some.turn(TURN.LEFT)

        print(f"{some.__class__}.show_speed() => {some.show_speed()}", end="\n\n")