import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import os

# GOAL: Approximate the integral of function f from lower bound a to upper bound b using Monte Carlo simulation

a = 0       # lower bound of integration
b = np.pi   # upper bound of integration
f = np.sin  # function to integrate
N = 10000   # sample size

def mcIntegrate(p):
    xrand = np.random.uniform(a, b, N)       # create array filled with random numbers within bounds
    integral = np.sum(f(xrand))                 # sum return values of function of each random number
    approx = integral * ((b - a) / float(N))    # scale integral by difference of bounds divided by sample size
    return approx


if __name__ == "__main__":
    
    # run simulation N times in parallel and store results in array
    with Pool(os.cpu_count() + 1) as pool:
        areas = pool.map(mcIntegrate, range(N))

    # graph approximation distribution
    plt.title("Distribution of Approximated Integrals")
    plt.hist(areas, bins=30, ec='black')
    plt.xlabel("Areas")
    plt.show()
