import timeit
import numpy as np
from numba import njit


def while_loop(n=100000000):
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    return s


def for_loop(n=100000000):
    s = 0
    for i in range(n):
        s += i
    return s


def sum_range(n=100000000):
    return sum(range(n))


def sum_numpy(n=100000000):
    return np.sum(np.arange(n))


def sum_numba(n=100000000):
    return np.sum(np.arange(n))


sum_numba_njit = njit()(sum_numba)


def main():
    # main
    print("wile loop \t\t", timeit.timeit(while_loop, number=1))
    print("for loop \t\t", timeit.timeit(for_loop, number=1))
    print("sum range \t\t", timeit.timeit(sum_range, number=1))
    print("sum numpy \t\t", timeit.timeit(sum_numpy, number=1))
    print("sum numba \t\t", timeit.timeit(sum_numba_njit, number=1))
    sum_numba_njit()
    print("That maen the numpy it's faster then numba")


# mian
if __name__ == '__main__':
    main()
