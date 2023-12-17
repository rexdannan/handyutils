import unittest
from unittest.mock import patch
from parameterized import parameterized
from io import StringIO
import sys
from gravitywattage import GravityWattage

class TestGravityWattage(unittest.TestCase):

    # Constants
    # Test data in the form of grade, velocity, mass, and wattage result
    WATTAGE_TESTS = [[.05, 5.36448, 85, 223.582205616],
                     [-.07, 3.33, 70, -160.01510805000004]
                    ]

    # Check wattage calculations
    def test_gravity_calcs(self):
        for grade, velocity, mass, wattage in self.WATTAGE_TESTS:
            watts = GravityWattage()
            self.assertEqual(watts.CalcWattage(grade, velocity, mass), wattage)

if __name__ == '__main__':
    unittest.main()