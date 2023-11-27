import argparse
import math
import re

# Common stuff
engtoiso = {16 : 305, 20 : 406, 24 : 507, 26 : 559, 27 : 630, 27.5 : 584, 29 : 622, 32 : 686, 36 : 787}
frtoiso = {400 : 340, 500 : 440, 650 : 584, 700 : 622}

class UserInput:
    def __init__(self):

        # Constants
        self.MMINCH = 25.4
        self.ISOREGEX = r"^\d{2}\-\d{3}$"
        self.ENGREGEX = r"^\d{2}\.?\d?\s[xX]\s\d\.?\d*$"
        self.FRREGEX = r"^\d{3}\s[xX]\s\d{2}[A-Da-d]$"

        # Variables
        self.tirewidth = 0
        self.wheelsize = 0

        # Define arguments
        self.parser = argparse.ArgumentParser(description="Handle tire size input.")
        self.parser.add_argument('size', type=str, help='Wheel size')

    def GetUserInput(self):

        self.args = self.parser.parse_args()

        if self.args:
            if re.search(self.ISOREGEX, self.args.size):
                self.tirewidth, self.wheelsize = map(int, self.args.size.split("-"))
            elif re.search(self.ENGREGEX, self.args.size):
                self.wheelsize, self.tirewidth = map(float, self.args.size.split("x"))
                self.tirewidth = self.tirewidth * self.MMINCH
                self.wheelsize = engtoiso.get(self.wheelsize)
            elif re.search(self.FRREGEX, self.args.size):
                self.wheelsizestr, self.tirewidthstr = map(str, self.args.size.split("x"))
                self.wheelsize = int(self.wheelsizestr)
                self.tirewidth = int(self.tirewidthstr.rstrip().lstrip()[:2])
                print(self.wheelsize, self.tirewidth)
                self.wheelsize = frtoiso.get(self.wheelsize)

class Wheel:
    def __init__(self, input):

        # Constants
        self.PI = 3.14159

        # Variables
        self.wheelsize = input.wheelsize
        self.tirewidth = input.tirewidth

    def Circumference(self):
        return (self.wheelsize + (2 * self.tirewidth)) * self.PI

if __name__ == '__main__':
    input = UserInput()
    input.GetUserInput()
    wheel = Wheel(input)
    print(round(wheel.Circumference(), 2))