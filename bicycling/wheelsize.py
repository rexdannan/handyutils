import math

PI = 3.14159

isosize = "30-622"
tiresize, wheelsize = map(int,isosize.split("-"))
circumference = (wheelsize + (2 * tiresize)) * PI
print(circumference)