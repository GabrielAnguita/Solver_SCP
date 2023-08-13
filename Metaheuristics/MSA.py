#SCA
import random
import math
import numpy as np
from scipy.special import gamma


# WIP, inline what should be inlined, functions are used to organize thought

def iterarMSA(maxIter, t, poblacion, solutionsRanking):
    beta = 1.5
    max_step = ...
    # at this step the population should already be binarized, if it needs to
    length = len(poblacion)
    for i, solucion in enumerate(poblacion[:length/2]):
        # Levy flight
        poblacion[i] = solucion + ...
    for i, solucion in enumerate(poblacion[(length/2) + 1:]):
        # Flight straight
        if random.random() > 0.5:
            poblacion[i] = ...
        else:
            poblacion[i] = ...
    return np.array(poblacion)
