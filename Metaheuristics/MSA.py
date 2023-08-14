# MSA
import random
import math
import numpy as np
from scipy.special import gamma


def iterarMSA(maxIter: int, t: int, population: np.array, bestSolution) -> np.array:
    """
    WIP: Moth Search Algorithm
    Implementation of https://link.springer.com/article/10.1007/s12293-016-0212-3

    TODO: SORT POPULATION BY FITNESS BEFORE ITERATING!
    
    TODO: Check if the constants defined below are supposed to be actual constants,
           or we got something wrong. Also, set them to more adequate values.
    """
    beta = 1.5
    max_step = 1
    s = 1
    lambda_factor = 1
    phi = 1
    levy = (
        (beta - 1) * gamma(beta - 1) * math.sin(math.pi * (beta - 1) / 2)
    ) / math.pi * s**beta
    length = len(population)
    
    """Metodo que se me ocurrio para hacer el sort (REVISAR)"""
     for t in range(MaxGen):   #MaxGen es el numero de generacion, que se le entrega como parametro
        x_fitness = [fitness(xi) for xi in x]
        sorted_indices = np.argsort(x_fitness)
        x = x[sorted_indices]
    """REVISAR"""
    
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
