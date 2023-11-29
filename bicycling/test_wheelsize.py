import unittest
from unittest.mock import patch
from parameterized import parameterized
from io import StringIO
import sys
import wheelsize

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
                        self.assertEqual(input.tirewidth, int(eng_size[:2]))
                        self.assertEqual(input.wheelsize, int(eng_size[3:6]))
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