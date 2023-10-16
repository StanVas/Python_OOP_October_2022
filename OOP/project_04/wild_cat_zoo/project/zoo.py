from project_04.wild_cat_zoo.project.animal import Animal
from project_04.wild_cat_zoo.project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity - len(self.animals) <= 0:
            return "Not enough space for animal"

        if self.__budget - price < 0:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity - len(self.workers) <= 0:
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)

        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)

        if self.__budget - salaries < 0:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tending_cost = sum(a.money_for_care for a in self.animals)

        if self.__budget - tending_cost < 0:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= tending_cost

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        # info = {"Lion": [], "Tiger": [], "Cheetah": []}
        # first way:
        # [info[x.__class__.__name__].append(str(x)) for x in self.animals]
        # second way:
        # for animal in self.animals:
        #     info[animal.__class__.__name__].append(str(animal))
        # third way:
        lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:"
        ]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(str(r) for r in result)

    def workers_status(self):
        # the same logic as in animal_status
        keepers = list(filter(lambda a: a.__class__.__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda a: a.__class__.__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda a: a.__class__.__name__ == "Vet", self.workers))

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(keepers)} Keepers:"
        ]
        result.extend(keepers)

        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)

        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return "\n".join(str(r) for r in result)
