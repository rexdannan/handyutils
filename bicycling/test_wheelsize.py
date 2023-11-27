import unittest
from unittest.mock import patch
from io import StringIO
import sys
import wheelsize

class TestWheelsize(unittest.TestCase):

    isotst = '30-622'

    @patch('sys.argv', ['wheelsize.py', isotst])
    def test_input(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            input = wheelsize.UserInput()
            input.GetUserInput()
            self.assertEqual(input.tirewidth, 30)
            self.assertEqual(input.wheelsize, 622)

    @patch('sys.argv', ['wheelsize.py', isotst])
    def test_wheel_iso(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            input = wheelsize.UserInput()
            input.GetUserInput()         
            wheel = wheelsize.Wheel(input)
            result = wheel.Circumference()
            self.assertEqual(result, 2142.56438)

if __name__ == '__main__':
    unittest.main()