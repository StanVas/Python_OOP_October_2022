from project_04.pizza_maker_second_try.project.animal import Animal
from project_04.pizza_maker_second_try.project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        elif self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)

        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)

        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tending_cost = sum(a.money_for_care for a in self.animals)

        if self.__budget < tending_cost:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= tending_cost

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda a: a.__class__.__name__ == 'Lion', self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == 'Tiger', self.animals))
        cheetah = list(filter(lambda a: a.__class__.__name__ == 'Cheetah', self.animals))

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:"
        ]

        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetah)} Cheetahs:")
        result.extend(cheetah)

        return '\n'.join(str(r) for r in result)

    def workers_status(self):
        keepers = list(filter(lambda w: w.__class__.__name__ == 'Keeper', self.workers))
        caretakers = list(filter(lambda w: w.__class__.__name__ == 'Caretaker', self.workers))
        vets = list(filter(lambda w: w.__class__.__name__ == 'Vet', self.workers))

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(keepers)} Keepers:"
        ]

        result.extend(keepers)

        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)

        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return '\n'.join(str(r) for r in result)
