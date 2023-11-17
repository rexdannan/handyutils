import argparse
import math

class Wheel:
    def __init__(self):

        # constants
        self.PI = 3.14159

        # Argument parsing
        self.parser = argparse.ArgumentParser(description="Handle tire size input.")
        self.parser.add_argument('size', type=str, help='ISO wheel size')
        self.args = self.parser.parse_args()

        self.tirewidth, self.wheelsize = map(int, self.args.size.split("-"))

    def Circumference(self):
        return (self.wheelsize + (2 * self.tirewidth)) * self.PI

if __name__ == '__main__':
    wheel = Wheel()
    print(wheel.Circumference())

