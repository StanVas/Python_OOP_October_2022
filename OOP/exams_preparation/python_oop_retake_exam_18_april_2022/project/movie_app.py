# from exams_preparation.python_oop_retake_exam_18_april_2022.project.movie_specification.movie import Movie
# from exams_preparation.python_oop_retake_exam_18_april_2022.project.user import User
from decorators_09_not_done.project import Movie
from decorators_09_not_done.project import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def find_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def register_user(self, username: str, age: int):
        if self.find_user(username):
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if not self.find_user(username):
            raise Exception("This user does not exist!")

        user = self.find_user(username)

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in user.movies_owned:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.find_user(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value

            elif key == 'year':
                movie.year = value

            elif key == 'age_restriction':
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.find_user(username)

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        movie_title = movie.title
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie_title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.find_user(username)

        if movie.owner == user:  # same as movie.owner.username == username
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_user(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."

        result = sorted([m for m in self.movies_collection], key=lambda x: ((-x.year), x.title))
        output = []
        for item in result:
            output.append(item.details())
        return '\n'.join(output)

    def __str__(self):
        users = []
        movies = []

        if len(self.users_collection) == 0:
            users.append("No users.")
        else:
            for user in self.users_collection:
                users.append(user.username)

        if len(self.movies_collection) == 0:
            movies.append("No movies.")
        else:
            for movie in self.movies_collection:
                movies.append(movie.title)

        return f"All users: {' ,'.join(users)}\nAll movies: {' ,'.join(movies)}"
