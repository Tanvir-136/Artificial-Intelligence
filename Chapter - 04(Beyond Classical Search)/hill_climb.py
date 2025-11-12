import matplotlib.pyplot as plt
import numpy as np
import random
import math

def fun(x):
    return -((x - 2) ** 2) + 4

def hill_climb(fun, init, step=1.0, iteration=100):
    x = init
    for i in range(iteration):
        print(f"Step {i+1}: f({x}) -> f({x+step}) OR f({x-step})")
        if fun(x) < fun(x+step):
            x += step
        elif fun(x) < fun(x-step):
            x -= step
        else:
            break
    return x
li = np.arange(-10, 10)

print(hill_climb(fun, random.randint(-10, 10), 1.5))

plt.plot(li, fun(li))
plt.grid()
plt.show()