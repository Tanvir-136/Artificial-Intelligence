import matplotlib.pyplot as plt
import numpy as np
import random
import math

def fun(x):
    return -((x - 2) ** 2) + 4


def local_beam_search(fun, k=2, start=-10, stop=10, step=1.0, iteration=50):
    # Start with k random states
    states = [random.uniform(start, stop) for _ in range(k)]

    for i in range(iteration):
        neighbors = []
        for s in states:
            neighbors.append(s + step)
            neighbors.append(s - step)

        all_states = states + neighbors

        states = sorted(all_states, key=lambda x: fun(x), reverse=True)[:k]

        print(f"[Beam] Step {i+1}: best={states[0]:.2f}, f(best)={fun(states[0]):.2f}")

    return max(states, key=fun)

print(local_beam_search(fun, 2, -10, 10, 1.5, 5))