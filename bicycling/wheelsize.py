import argparse
import math

class UserInput:
    def __init__(self):

        # Set variables
        self.tirewidth = 0
        self.wheelsize = 0

        # Define arguments
        self.parser = argparse.ArgumentParser(description="Handle tire size input.")
        self.parser.add_argument('size', type=str, help='Wheel size')

    def GetUserInput(self):

        self.args = self.parser.parse_args()

        if self.args:
            self.tirewidth, self.wheelsize = map(int, self.args.size.split("-"))

class Wheel:
    def __init__(self, input):

        # constants
        self.PI = 3.14159

    def Circumference(self):
        return (self.wheelsize + (2 * self.tirewidth)) * self.PI

if __name__ == '__main__':
    wheel = Wheel()
    print(round(wheel.Circumference(), 2))

