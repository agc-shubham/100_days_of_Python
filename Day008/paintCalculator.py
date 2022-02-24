# You are painting a wall. The instructions on the paint can says that 
# 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, 
# calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5
import math

def paint_calc(height, width, cover):
    area = height * width
    nofCans = math.ceil(area / cover)
    print(f"Number of cans required is {nofCans}")
    


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)