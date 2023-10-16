from abc import abstractmethod, ABC


class BaseDuck(ABC):
    @staticmethod
    def quack(self):
        pass


class WalkingDuck(ABC):
    @staticmethod
    def walk(self):
        pass


class FlyingDuck(ABC):
    @staticmethod
    def fly(self):
        pass


class RubberDuck(BaseDuck):
    @staticmethod
    def quack(self):
        return "Squeek"


class RobotDuck(BaseDuck, FlyingDuck, WalkingDuck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    def quack(self):
        return 'Robotic quacking'

    def walk(self):
        return 'Robotic walking'

    def fly(self):
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


robot = RobotDuck()
print(robot.fly())
print(robot.fly())
print(robot.fly())
print(robot.height)
