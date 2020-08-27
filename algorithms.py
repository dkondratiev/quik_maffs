def euclidean_gcd(a: int, b: int) -> int:
    """
    Finds greatest common divisor of two numbers (Euclidean algorithm)
    >>> euclidean_gcd(0, 0)
    0
    >>> euclidean_gcd(0, 10)
    10
    >>> euclidean_gcd(48, 60)
    12
    """

    if a == 0 or b == 0:
        return a + b
    if a == b:
        return a
    if a < b:
        a, b = b, a
    mod = a % b
    if mod == 0:
        return b
    return euclidean_gcd(b, mod)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
