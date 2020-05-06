import random


def set_seed(seed):
    random.seed(seed)


def get_pi(rounds=10000, report_step=1000):
    """
    Estimates pi by calculating the probability of random point to be in sector of circle with center in (0, 0)
    :param rounds: number of rounds to simulate
    :param report_step: step to report intermediary results
    :return: estimation of pi
    """
    trials = 0
    in_circle = 0
    for round_number in range(rounds):
        x, y = random.random(), random.random()
        in_circle += int(x ** 2 + y ** 2 < 1)
        trials += 1
        if report_step is not None and round_number % report_step == 0 and round_number > 0:
            print(f'pi after iteration {round_number}: {in_circle / trials * 4}')
    return in_circle / trials * 4


def get_e(rounds=10000, report_step=100):
    """
    Estimates e by calculating the average of how many random numbers need to be draws for their sum to be higher than 1
    :param rounds: number of rounds to simulate
    :param report_step: step to report intermediary results
    :return: estimation of e
    """
    draws_needed = 0
    for round_number in range(rounds):
        sum_of_randoms = 0
        while sum_of_randoms < 1:
            sum_of_randoms += random.random()
            draws_needed += 1
        if report_step is not None and round_number % report_step == 0 and round_number > 0:
            print(f'e after iteration {round_number}: {draws_needed / round_number}')
    return draws_needed / rounds
