# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen

from abc import ABC, abstractmethod

class Person:
    def __init__(self, id: str, name: str, is_a_student: bool):
        self.id = id
        self.name = name
        self.is_a_student = is_a_student

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return len(name.split()) >= 2

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if not self.is_valid_name(new_name):
            raise ValueError(f"Invalid name: {new_name}")
        self.__name = new_name

class Residence(ABC):
    def __init__(self, address: str, area: float, number_of_rooms: int):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}

    @property
    def number_of_occupants(self) -> int:
        return len(self.__occupants)

    @property
    def maximum_occupants(self) -> int:
        by_area = self.area // 20
        by_rooms = self.number_of_rooms * 2
        return int(min(by_area, by_rooms))

    def register_resident(self, person: Person):
        if person.id in self.__occupants:
            return
        if self.number_of_occupants >= self.maximum_occupants:
            raise RuntimeError("Not enough room for another resident")
        self.__occupants[person.id] = person

    def unregister_resident(self, id: str):
        if id in self.__occupants:
            del self.__occupants[id]

    @property
    def resident_names(self) -> list:
        return [person.name for person in self._occupants.values()]

    @abstractmethod
    def calculate_value(self) -> float:
        pass

class Villa(Residence):
    def __init__(self, address: str, area: float, number_of_rooms: int, garage_capacity: int):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self) -> float:
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)

class StudentKot(Residence):
    def __init__(self, address: str, area: float):
        super().__init__(address, area, number_of_rooms=1)

    def register_resident(self, person: Person):
        if not person.is_a_student:
            raise RuntimeError("Only students can register in a StudentKot")
        super().register_resident(person)

    def calculate_value(self) -> float:
        return 150000 + (750 * self.area)
    
