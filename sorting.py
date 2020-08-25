import time
import numpy as np

def is_sorted(l: list) -> bool:
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            return False
    return True

def is_sorted_recursive(l: list) -> bool:
    """
    Quite useless for bigger lists as it will hit recursion limit
    """
    if len(l) in (0, 1):
        return True
    if l[0] > l[1]:
        return is_sorted_recursive(l[1:])
    else:
        return False

l = sorted(np.random.random(size=100000), reverse=True)