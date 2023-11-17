import argparse
import math

# Constants
PI = 3.14159

# Argument parsing
parser = argparse.ArgumentParser(description="Handle tire size input.")

parser.add_argument('size', type=str, help='ISO wheel size')

args = parser.parse_args()

size = args.size

tirewidth, wheelsize = map(int, size.split("-"))
circumference = (wheelsize + (2 * tirewidth)) * PI
print(circumference)