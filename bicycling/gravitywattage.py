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

    def __init__(self):
        self.grade = 0
        self.speed = 0
        self.mass = 0

    def ProcessInput(self):
        pass

    def CalcWattage(self):
        return self.grade * self.speed * self.mass * GRAVITY


