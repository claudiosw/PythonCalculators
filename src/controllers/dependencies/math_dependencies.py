import math
import numpy as np

def calculate_sqrt(input: float) -> float:
    return math.sqrt(input)

def calculate_average(list: list[float]) -> float:
    numpy_array = np.array(list) 
    return np.average(numpy_array)
