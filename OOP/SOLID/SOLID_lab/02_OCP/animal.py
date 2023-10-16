from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def animal_sound(self):
        ...


class Dog(Animal):
    def animal_sound(self):
        return "Woof"


class Cat(Animal):
    def animal_sound(self):
        return "Meow"


class Chicken(Animal):
    def animal_sound(self):
        return "Clutch"


def make_sound(animals_lst: list):
    for animal in animals_lst:
        print(animal.animal_sound())


animals = [Cat(), Dog(), Chicken()]
make_sound(animals)
