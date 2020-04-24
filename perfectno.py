def is_perfect_cube(number):
    number = abs(number)
    return round(number ** (1/3)) ** 3 == number

def qsqsq() -> [int]:
    perf_sq = list()
    x = 1
    while x*x < 1000:
        num = x*x
        i=1
        while i*i < num:
            if is_perfect_cube(num-i*i):
                perf_sq.append(num)
                break
            i+=1
        x+=1
    return perf_sq

print(qsqsq())

#----------------------------------------

LIMIT = 1000
CUBE_LIMIT = int(LIMIT ** 0.33 + 0.5)
SQUARE_LIMIT = int(LIMIT ** 0.5 + 0.5)
cubes = [a ** 3 for a in range(1, CUBE_LIMIT + 1)] #since we need only till 1000
squares = [a * a for a in range(1, SQUARE_LIMIT + 1)]
 
from itertools import products as cp

print(sorted(set(x + y for x, y in cp(cubes, squares)) & set(squares)))