import random, numpy as np

def random_log_uniform(min_value = 10e-5, max_value = 10e-3):
    return np.exp(np.log(min_value) + random.random()*(np.log(max_value) - np.log(min_value)))
