import argparse
import math
import re
import sys

# Common stuff
MMINCH = 25.4
MMCM = 10

engtoiso = {16 : 305, 20 : 406, 24 : 507, 26 : 559, 27 : 630, 27.5 : 584, 29 : 622, 32 : 686, 36 : 787}
frtoiso = {400 : 340, 500 : 440, 650 : 584, 700 : 622}

unit_input = ["mm", "cm", "inch"]

help_input = ["-h", "help"]
help_text = """

This utility calculates a bicycle wheel's circumference based on tire size and width.
Input can be in ISO, English, and French format:

ISO in millimeters: wheelsize.py 30-622 mm
English in centimeters: wheelsize.py 27.5x2.8 cm
French in inches: wheelsize.py 700x30C inch
"""

class UserInput:
    def __init__(self):

        # Constants       
        self.ISOREGEX = r"^\d{2}\-\d{3}$"
        self.ENGREGEX = r"^\d{2}\.?\d?[xX]\d(\.\d\d?)?$"
        self.FRREGEX = r"^\d{3}[xX]\d{2}[A-Da-d]$"

        # Variables
        self.tirewidth = 0
        self.wheelsize = 0
        self.unit = ""
        self.testtext = "HEY THERE!"

        # Define arguments
        self.parser = argparse.ArgumentParser(description="Handle tire size input.")
        self.parser.add_argument('size', type=str, help='Tire size in ISO, English, or French format')
        self.parser.add_argument('unit', type=str, help='Units in mm, cm, or inch')

    def GetUserInput(self):

        self.args = self.parser.parse_args()

        # Process size 
        if self.args.size:
            if re.search(self.ISOREGEX, self.args.size):
                self.tirewidth, self.wheelsize = map(int, self.args.size.split("-"))
            elif re.search(self.ENGREGEX, self.args.size):
                self.wheelsize, self.tirewidth = map(float, self.args.size.split("x"))
                self.tirewidth = self.tirewidth * MMINCH
                self.wheelsize = engtoiso.get(self.wheelsize)
                if not self.wheelsize:
                    sys.exit("Please enter a valid English wheel size.")
            elif re.search(self.FRREGEX, self.args.size):
                self.wheelsizestr, self.tirewidthstr = map(str, self.args.size.split("x"))
                self.wheelsize = int(self.wheelsizestr)
                self.tirewidth = int(self.tirewidthstr.rstrip().lstrip()[:2])
                self.wheelsize = frtoiso.get(self.wheelsize)
                if not self.wheelsize:
                    sys.exit("Please enter a valid French wheel size.")
            elif self.args.size.lower() in help_input:
                print(help_text)
            else:
                sys.exit("The input format was not recognized. Please enter \"wheelsize.py help\" for more details.")
        
        # Process unit size
        if self.args.unit.lower() in unit_input:
            self.unit = self.args.unit.lower()
        else:
            sys.exit("The unit format was not recoginzed. Please enter \"wheelsize.py help\" for more details.")

class Wheel:
    def __init__(self, input):

        # Constants
        self.PI = 3.14159

        # Variables
        self.wheelsize = input.wheelsize
        self.tirewidth = input.tirewidth
        self.unit = input.unit

    def Circumference(self):
        circumference = (self.wheelsize + (2 * self.tirewidth)) * self.PI
        if self.unit == "cm":
            circumference = circumference / MMCM
        elif self.unit == "inch":
            circumference = circumference / MMINCH

        return circumference

if __name__ == '__main__':
    input = UserInput()
    input.GetUserInput()
    wheel = Wheel(input)
    circumference = wheel.Circumference()
    if circumference:
        print(round(circumference, 2))