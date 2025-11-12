import matplotlib.pyplot as plt
import numpy as np
import random
import math

def fun(x):
    return -((x - 2) ** 2) + 4

def hill_climb_random(fun, start=-10, stop=10, step=1.0, iteration=100):
    x = random.randint(start, stop)
    di = {}
    for i in range(iteration):
        print(f"Step {i+1}: f({x}) - f({x+step}) - f({x-step})")
        if fun(x) < fun(x+step):
            x += step
        elif fun(x) < fun(x-step):
            x -= step
        else:
            di[x] = fun(x)
            x = random.randint(start, stop)
    print(di)
    return [i for i, j in di.items() if j == max(di.values())][0]

print(hill_climb_random(fun, -10, 10, 1.5, 5))