import unittest
from unittest.mock import patch
from parameterized import parameterized
from io import StringIO
import sys
import wheelsize

# Constants
MMINCH = 25.4
MMCM = 10
engtoiso = {16 : 305, 20 : 406, 24 : 507, 26 : 559, 27 : 630, 27.5 : 584, 29 : 622, 32 : 686, 36 : 787}
frtoiso = {400 : 340, 500 : 440, 650 : 584, 700 : 622}

class TestWheelsize(unittest.TestCase):

    validunits = ["mm", "MM", "cm", "CM", "inch", "INCH"]
    validiso = ["54-550",  "70-584", "30-622"]
    valideng = ["26x2", "26x2.1", "27.5x2.8", "29x2.4"]
    validfr = ["650x42B","700x30c"]

    def test_valid_iso_input(self):
        for iso_size in self.validiso:
            for unit in self.validunits:
                with patch('sys.argv', ['wheelsize.py', iso_size, unit]):
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        input = wheelsize.UserInput()
                        input.GetUserInput()
                        self.assertEqual(input.tirewidth, int(iso_size[:2]))
                        self.assertEqual(input.wheelsize, int(iso_size[3:6]))
                        self.assertEqual(input.unit, unit.lower())

    def test_valid_eng_input(self):
        for eng_size in self.valideng:
            for unit in self.validunits:
                with patch('sys.argv', ['wheelsize.py', eng_size, unit]):
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        input = wheelsize.UserInput()
                        input.GetUserInput()
                        eng_wheel, eng_width = map(float, eng_size.split("x"))
                        eng_wheel = engtoiso.get(eng_wheel)
                        eng_width *= MMINCH
                        self.assertEqual(input.tirewidth, eng_width)
                        self.assertEqual(input.wheelsize, eng_wheel)
                        self.assertEqual(input.unit, unit.lower())

    def test_valid_fr_input(self):
        for fr_size in self.validfr:
            for unit in self.validunits:
                with patch('sys.argv', ['wheelsize.py', fr_size, unit]):
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        input = wheelsize.UserInput()
                        input.GetUserInput()
                        fr_wheel, fr_width = map(str, fr_size.split("x"))
                        fr_width = int(fr_width[:2])
                        fr_wheel = float(fr_wheel)
                        fr_wheel = frtoiso.get(fr_wheel)
                        self.assertEqual(input.tirewidth, fr_width)
                        self.assertEqual(input.wheelsize, fr_wheel)
                        self.assertEqual(input.unit, unit.lower())

    # @parameterized.expand([(isosize, unit) for isosize in validiso for unit in validunits])
    # @patch('sys.argv', ['wheelsize.py', isosize, unit])
    # def test_input(self):
    #     with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
    #         print("Hello")
    #         input = wheelsize.UserInput()
    #         input.GetUserInput()
    #         self.assertEqual(input.tirewidth, 30)
    #         self.assertEqual(input.wheelsize, 622)

    # @patch('sys.argv', ['wheelsize.py', "30-622", "mm"])
    # def test_wheel_iso(self):
    #     with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
    #         input = wheelsize.UserInput()
    #         input.GetUserInput()         
    #         wheel = wheelsize.Wheel(input)
    #         result = wheel.Circumference()
    #         self.assertEqual(result, 2142.56438)

if __name__ == '__main__':
    unittest.main()