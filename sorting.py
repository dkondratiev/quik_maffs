import random

def is_sorted(l: list) -> bool:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def is_sorted_recursive(l: list) -> bool:
    """
    Quite useless for bigger lists as it will hit recursion limit
    """
    if len(l) < 2:
        return True
    if l[0] < l[1]:
        return is_sorted_recursive(l[1:])
    else:
        return False

def quick_sort(l: list) -> list:
    """
    Does not reliably work for lists with repeating elements
    :param l:
    :return:
    """
    if len(l) < 2:
        return l
    else:
        pivot = l[random.randint(0, len(l) - 1)]
        less = []
        equal = []
        greater = []
        for i in l:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([3, 3, 2, 1, 1]))