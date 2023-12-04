import unittest
from unittest.mock import patch
from parameterized import parameterized
from io import StringIO
import sys
from wheelsize import Wheel, UserInput

# Constants
MMINCH = 25.4
MMCM = 10
engtoiso = {16 : 305, 20 : 406, 24 : 507, 26 : 559, 27 : 630, 27.5 : 584, 29 : 622, 32 : 686, 36 : 787}
frtoiso = {400 : 340, 500 : 440, 650 : 584, 700 : 622}

class SampleInput:
                  
    # Variables
    tirewidth = 0
    wheelsize = 0
    unit = 0

    def __init__(self, tirewidth, wheelsize, unit):
        self.tirewidth = tirewidth
        self.wheelsize = wheelsize
        self.unit = unit

class TestWheelsize(unittest.TestCase):

    validunits = ["mm", "MM", "cm", "CM", "inch", "INCH"]
    invalidunits = ["inck", "", "car"]
    validiso = ["54-550",  "70-584", "30-622", "622-30", ""]
    valideng = ["26x2", "26x2.1", "27.5x2.8", "29x2.4", "2x21"]
    validfr = ["650x42B", "700x30c", "6Bx300"]
    invalidinput = ["6Bx300", "2x21", "700-30", "@#", ""]
    circumferences = {"mm" : 2142.56438, "MM" : 2142.56438, "cm" : 214.25643799999997, "CM" : 214.25643799999997, "inch" : 84.3529283464567, "INCH" : 84.3529283464567}

    # ISO sizing tests
    def test_valid_iso_input(self):
        for iso_size in self.validiso:
            for unit in self.validunits:
                with patch('sys.argv', ['wheelsize.py', iso_size, unit]):
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        if self.assertRaises(SystemExit):
                            pass
                        else:
                            input = wheelsize.UserInput()
                            input.GetUserInput()
                            self.assertEqual(input.tirewidth, int(iso_size[:2]))
                            self.assertEqual(input.wheelsize, int(iso_size[3:6]))
                            self.assertEqual(input.unit, unit.lower())

    # English sizing tests
    def test_valid_eng_input(self):
        for eng_size in self.valideng:
            for unit in self.validunits:
                with patch('sys.argv', ['wheelsize.py', eng_size, unit]):
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        if self.assertRaises(SystemExit):
                            pass
                        else:
                            input = wheelsize.UserInput()
                            input.GetUserInput()
                            eng_wheel, eng_width = map(float, eng_size.split("x"))
                            eng_wheel = engtoiso.get(eng_wheel)
                            eng_width *= MMINCH
                            self.assertEqual(input.tirewidth, eng_width)
                            self.assertEqual(input.wheelsize, eng_wheel)
                            self.assertEqual(input.unit, unit.lower())

    # French sizing tests
    def test_valid_fr_input(self):
        for fr_size in self.validfr:
            for unit in self.validunits:
                with patch('sys.argv', ['wheelsize.py', fr_size, unit]):
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        if self.assertRaises(SystemExit):
                            pass
                        else:
                            input = wheelsize.UserInput()
                            input.GetUserInput()
                            fr_wheel, fr_width = map(str, fr_size.split("x"))
                            fr_width = int(fr_width[:2])
                            fr_wheel = float(fr_wheel)
                            fr_wheel = frtoiso.get(fr_wheel)
                            self.assertEqual(input.tirewidth, fr_width)
                            self.assertEqual(input.wheelsize, fr_wheel)
                            self.assertEqual(input.unit, unit.lower())

    # Check circumference calculations
    def test_circumference_calcs(self):
        for unit in self.validunits:
            testinput = SampleInput(30, 622, unit.lower())
            wheel = Wheel(testinput)
            print(unit, wheel.Circumference())
            self.assertEqual(wheel.Circumference(), self.circumferences.get(unit))

if __name__ == '__main__':
    unittest.main()