import matplotlib.pyplot as plt
import numpy as np
import random
import math

def fun(x):
    return -((x - 2) ** 2) + 4

def stochastic_hill_climb(fun, init, step=1.0, iteration=100):
    x = init
    for i in range(iteration):
        neighbors = [x + step, x - step]
        next_x = random.choice(neighbors)
        # print(f"Step {i+1}: f({x}) -> f({next_x})")
        if fun(next_x) > fun(x):
            x = next_x
    return x

print(stochastic_hill_climb(fun, random.randint(-10, 10), 1.5))