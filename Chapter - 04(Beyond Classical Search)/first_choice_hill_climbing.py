import matplotlib.pyplot as plt
import numpy as np
import random
import math

def fun(x):
    return -((x - 2) ** 2) + 4

def first_choice_hill_climbing(fun, init, step=1.0, max_iterations=1000):
    current_state = init
    for _ in range(max_iterations):
        neighbors = [current_state + step, current_state - step]
        random.shuffle(neighbors)
        for neighbor in neighbors:
            if fun(neighbor) > fun(current_state):
                current_state = neighbor
                break
        else:
            break  # No better neighbor found
    return current_state

print(first_choice_hill_climbing(fun, random.randint(-10, 10), 1.5))