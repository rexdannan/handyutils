import argparse
import math
import re
import sys
from wheelsize import Wheel, UserInput

class GDUserInput(UserInput):

    # Constants
    MINGEARTEETH = 10

    def __init__(self):
        super().__init__()

        self.chainring = 0
        self.cog = 0

        self.parser.add_argument('chainring', type=int, help='Number of teeth in the front chainring')
        self.parser.add_argument('cog', type=int, help='Number of teeth in the rear cog')

    def GDGetUserInput(self):
        super().GetUserInput()

        self.chainring = self.args.chainring
        self.cog = self.args.cog

        if not self.chainring or not self.cog:
            sys.exit("Please enter both a chainring and cog tooth count")
        elif self.MINGEARTEETH > (self.chainring or self.cog):
            sys.exit(f"Please enter tooth counts of {self.MINGEARTEETH} or greater")

class GearDistance(Wheel):
    def __init__(self, input):
        Wheel.__init__(self, input)

        # Variables
        self.chainring = input.chainring
        self.cog = input.cog

    def CalcDistance(self):
        return self.Circumference() * (self.chainring / self.cog)

if __name__ == '__main__':
    input = GDUserInput()
    input.GDGetUserInput()
    geardistance = GearDistance(input)
    distance = geardistance.CalcDistance()
    if distance:
        print(round(distance, 2))