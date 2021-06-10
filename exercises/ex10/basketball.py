"""A class to model a basketball game."""

__author__ = "YOUR 9-DIGIT PID"


# TODO 1: Define the BBallGame class, and its logic, here.
class BBallGame:
    biscuits: bool
    points: int
    winning_team: str
    losing_team: str

# Define our own constructor 
    def __init__(self, points: int, winning_team: str, losing_team: str): 
        self.x = points
        self.y = winning_team
        self.z = losing_team
        self.biscuits = False

    def check_points(self) -> None :
        if self.x >= 100:
            self.biscuits = True
        return None

    def winner(self) -> str:
        if self.y == "UNC":
            if self.z == "DUKE":
                result = "GTHD"
            elif self.z != "DUKE":
                result = "woohoo"
        elif self.z == "UNC":
            result = "daggum"
        return result

    
    def reset_points(self) -> int:
        result: int = self.x
        self.x = 0.0
        return result
