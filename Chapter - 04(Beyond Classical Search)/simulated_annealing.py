import matplotlib.pyplot as plt
import numpy as np
import random
import math

def fun(x):
    return -((x - 2) ** 2) + 4

def simulated_annealing(fun, start=-10, stop=10, step=1.0, temparature=100, cooling=0.95):
    x = random.uniform(start, stop)
    best = x
    i = 0
    while temparature > 0.1:
        i += 1
        # Small random move (neighbor)
        x_new = x + random.uniform(-step, step)
        if x_new < start: x_new = start
        if x_new > stop: x_new = stop

        delta = fun(x_new) - fun(x)

        # Accept if better or with probability exp(delta/T)
        if delta > 0 or random.random() < math.exp(delta / temparature):
            x = x_new
            if fun(x) > fun(best):
                best = x

        # print(f"[SA] Step {i}: T={temparature:.2f}, x={x:.2f}, f(x)={fun(x):.2f}")
        temparature *= cooling
    return best

print(simulated_annealing(fun, -10, 10, 1.0, 100, 0.9))