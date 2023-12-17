# This is a simple python utility to calculate the wattage needed to overcome a grade
# 
# Formula used: watts(PE) = slope * speed in meters/sec * total mass in KG * 9.8 m/sec^2

import argparse
import sys
import math

class GravityWattage:

    # Constants
    GRAVITY = 9.80665
    MILEHMETERS = 0.44704
    KMHMETERS = 0.2777778
    LB2KG = 0.4535924

    HELP_TEXT = """
    This utility calculates the wattage required to address gravitational force for a given grade and rider/bicycle mass.
    It does not factor in rolling resistance, drivetrain losses, and wind resistence. Input format:
    
    Syntax: gravitywattage.py <grade> <speed> <weight>

    Examples:
    gravitywattage.py .05 12m 180lb - 5% grade, 12 mph, 180 pounds
    gravitywattage.py .07 20k 80kg - 7% grade (downhill), 20 kilometers, 80 kilograms
    """

    def __init__(self):
        # Parameters
        self.parser = argparse.ArgumentParser(description=self.HELP_TEXT)
        self.parser.add_argument('grade', type=str, help='Grade %% expressed as a decimal')
        self.parser.add_argument('speed', type=str, help='Speed expressed as mph or km')
        self.parser.add_argument('mass', type=str, help='Bicycle and rider weight expressed as lbs or kg')

        self.grade = 0
        self.speed = 0
        self.mass = 0

    def ProcessInput(self):

        self.args = self.parser.parse_args()

        # Process grade or help request
        if self.args.grade:
            try:
                self.grade = float(self.args.grade)
            except:
                sys.exit("Please enter a grade between -1.00 and 1.00.")
            if self.grade > 1 or self.grade < -1:
                sys.exit("Please enter a grade between -1.00 and 1.00.")

        # Process speed
        if self.args.speed:
            speedunit = self.args.speed[-1].lower()
            if speedunit in ["m", "k"]:
                try:
                    self.speed = float(self.args.speed[:-1])
                except:
                    sys.exit("Please enter a number for speed.")
                
                # Convert speed to meters per second
                if speedunit == "m":
                    self.speed *= self.MILEHMETERS
                else:
                    self.speed *= self.KMHMETERS
            else:
                sys.exit("Suffix the distance with \"m\" for miles or \"k\" for kilometers.")

        # Process mass
        if self.args.mass:
            massunit = self.args.mass[-2:].lower()
            if massunit in ["kg", "lb"]:
                try:
                    self.mass = float(self.args.mass[:-2])
                except:
                    sys.exit("Please enter a number for mass.")
                if massunit == "lb":
                    self.mass *= self.LB2KG
            else:
                sys.exit("Enter a mass unit as \"lb\" for pounds or \"kg\" for kilograms")

    def CalcWattage(self, grade=0, speed=0, mass=0):
        if grade:
            self.grade = grade
        if speed:
            self.speed = speed
        if mass:
            self.mass = mass 
        return self.grade * self.speed * self.mass * self.GRAVITY
    
if __name__ == '__main__':
    watts = GravityWattage()
    watts.ProcessInput()
    print(watts.CalcWattage())