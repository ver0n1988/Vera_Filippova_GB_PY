from abc import ABC, abstractmethod

class MaterialLenSolver:
    __length: float = 0
    __coat_list = []
    __costume_list = []

    @property
    def length(self):
        return self.__length

    @property
    def node_list(self):
        return {"coats": self.__coat_list, "costumies": self.__costume_list}

    @node_list.setter
    def node_list(self, other, add=True):
        if other.__class__ is Coat:
            if add:
                self.__coat_list.append(other.get_name())
            else:
                self.__coat_list.remove(other.get_name())
        elif other.__class__ is Costume:
            if add:
                self.__costume_list.append(other.get_name())
            else:
                self.__costume_list.remove(other.get_name())
        else:
            raise ValueError("Unknow cloth  type")

    @length.setter
    def length(self, in_len: float):
        self.__length += in_len

    def __iadd__(self, other):
        self.length = other.material_length()
        self.node_list = other
        return self

    def __isub__(self, other):
        self.length = - other.material_length()
        if other.__class__ is Coat and other.get_name() in self.__costume_list:
            self.__costume_list.remove(other.get_name())
        elif other.__class__ is Costume and other.get_name() in self.__coat_list:
            self.__coat_list.remove(other.get_name())
        return self

class Cloth(ABC):
    name: str

    def get_name(self):
        return self.name

    def material_length(self):
        pass

class Coat(Cloth):
    def __init__(self, name, size) -> None:
        super().__init__()
        self.name = name
        self.size = size

    def material_length(self):
        return self.size * 6.5 + 0.5

class Costume(Cloth):
        def __init__(self, name, height) -> None:
            super().__init__()
            self.name = name
            self.height = height

        def material_length(self):
            return 2 * self.height + 0.3

if __name__ == "__main__":
        mtr_solver = MaterialLenSolver()

        mtr_solver += Coat("For user 001", 12)
        mtr_solver += Costume("For film 01", 131)
        mtr_solver += Costume("For film 02", 189)
        mtr_solver += Costume("For film 03", 95)
        mtr_solver += Costume("For film 03", 230)
        mtr_solver += Costume("For film 04", 170)
        mtr_solver += Costume("For film 05", 108)
        mtr_solver += Coat("For user 111", 11)
        mtr_solver += Coat("For user 101", 29)
        mtr_solver += Coat("For user 011", 16)

        print(f"{mtr_solver.length} meters for {mtr_solver.node_list}")