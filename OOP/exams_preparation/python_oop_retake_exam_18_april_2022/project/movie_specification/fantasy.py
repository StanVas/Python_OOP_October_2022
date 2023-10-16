# from exams_preparation.python_oop_retake_exam_18_april_2022.project.movie_specification.movie import Movie
# from exams_preparation.python_oop_retake_exam_18_april_2022.project.user import User
from decorators_09_not_done.project import Movie
from decorators_09_not_done.project import User


class Fantasy(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 6):
        super().__init__(title, year, owner, age_restriction)
        
    @property
    def age_restriction(self):
        return self.__age_restriction
    
    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}," \
               f" Likes:{self.likes}, Owned by:{self.owner.username}"
