# MSA
import random
import math
import numpy as np
from scipy.special import gamma


def iterarMSA(maxIter, t, population, fitnesses, bestSolution):
    """
    WIP: Moth Search Algorithm
    Implementation of https://link.springer.com/article/10.1007/s12293-016-0212-3

    TODO: SORT POPULATION BY FITNESS BEFORE ITERATING!

    TODO: Check if the constants defined below are supposed to be actual constants,
           or we got something wrong. Also, set them to more adequate values.
    """
    beta = 1.5
    max_step = 1
    s = 3
    phi = 0.615
    levy = (
        ((beta - 1) * gamma(beta - 1) * math.sin(math.pi * (beta - 1) / 2))
        / math.pi
        * s**beta
    )
    length = len(population)

    sorted_indices = np.argsort(fitnesses)
    population = population[sorted_indices]

    for i, candidate in enumerate(population[: length // 2]):
        # Levy flight
        population[i] = candidate + ((max_step / (t+1)**2) * levy)
    for i, candidate in enumerate(population[(length // 2) + 1 :]):
        # Straight flight
        lambda_factor = random.uniform(0, 1)
        if random.random() > 0.5:
            population[i] = lambda_factor * (
                candidate + phi * (bestSolution - candidate)
            )
        else:
            population[i] = lambda_factor * (
                candidate + (1 / phi) * (bestSolution - candidate)
            )
    return np.array(population)
