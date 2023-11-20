import unittest
from unittest.mock import patch
from io import StringIO
import sys
import wheelsize

class TestWheelsize(unittest.TestCase):

    @patch('sys.argv', ['wheelsize.py', '30-622'])
    def test_wheel(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            wheel = wheelsize.Wheel()
            result = wheel.Circumference()
            self.assertEqual(result, 2142.56438)


    # @patch('sys.argv', ['my_script.py', '--input', 'test_input'])
    # def test_main_with_input(self):
    #     with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
    #         my_script.main()
    #         result = mock_stdout.getvalue().strip()
    #         self.assertEqual(result, 'Received input: test_input')

if __name__ == '__main__':
    unittest.main()