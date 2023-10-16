# from exams_preparation.python_oop_retake_exam_23_august_2021.project.astronaut.astronaut import Astronaut
from decorators_09_not_done.project import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name, oxygen=50):
        super().__init__(name, oxygen)

    def breathe(self):
        pass
