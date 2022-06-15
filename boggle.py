from turtle import position

import random

class Cube:
    def __init__(self, position, value):
        self.position = position
        self.value = value

    def roll(self):
        print(f"This cube has position {self.position}")
        print(f"Cube {self.position} has value {self.value}")

    def setBoard(self):
        print(self.value)

letters = "abcdefghijklmnopqrstuvwxyz"

for num in range(1, 13):
    randomLetter = random.choice(letters)
    c = Cube(num, randomLetter)
    # c.roll()
    c.setBoard()


