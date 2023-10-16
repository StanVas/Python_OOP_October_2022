from exams_preparation.Python_oop_exam_14_august_2022.project.horse_specification.horse import Horse
# from decorators_09_not_done.project import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed += 2
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
