from project_04.wild_cat_zoo.project.worker import Worker


class Caretaker(Worker):
    # pass  # can go just with pass because the class inherit the same attributes
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age, salary)
