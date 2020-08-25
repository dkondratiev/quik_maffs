from typing import Union

def sum_recursive(l: list) -> float:
    if not l:
        return 0
    return l[0] + sum_recursive(l[1:])

def len_recursive(l: list) -> int:
    if not l:
        return 0
    return 1 + len_recursive(l[1:])

def max_recursive(l: list) -> Union[float, None]:
    if not l:
        return None
    if len(l) == 1:
        return l[0]
    rec_max = max_recursive(l[1:])
    if rec_max > l[0]:
        return rec_max
    return l[0]

