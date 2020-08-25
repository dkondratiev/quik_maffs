def sum_recursive(l: list) -> float:
    if len(l) == 0:
        return 0
    return l[0] + sum_recursive(l[1:])
