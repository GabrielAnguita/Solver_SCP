#SCA
import random
import math
import numpy as np
from scipy.special import gamma


def iterarMSA(maxIter: int, t: int, population: np.array, bestSolution) -> np.array:
    # TODO: SORT POPULATION BY FITNESS BEFORE ITERATING!
    beta = 1.5
    max_step = 1
    s = 1
    lambda_factor = ...
    phi = ...
    levy = (
        (beta - 1) * gamma(beta - 1) * math.sin(math.pi * (beta - 1) / 2)
    ) / math.pi * s**beta
    length = len(population)
    for i, candidate in enumerate(population[:length//2]):
        # Levy flight
        population[i] = candidate + (
            (max_step / t**2) * levy
        )
    for i, candidate in enumerate(population[(length//2) + 1:]):
        # Straight flight
        if random.random() > 0.5:
            population[i] = lambda_factor * (
                candidate + phi * (bestSolution - candidate)
            )
        else:
            population[i] = lambda_factor * (
                candidate + (1 / phi) * (bestSolution - candidate)
            )
    return np.array(population)
