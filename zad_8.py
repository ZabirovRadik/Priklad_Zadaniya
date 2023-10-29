"""Module providing a function printing python version 3.11.5."""
import logging
import argparse
import random
import math
from time import time
from concurrent.futures import ThreadPoolExecutor


start = time()
logging.basicConfig(level=logging.DEBUG)


def pi_Monte_Karlo(points: int) -> int:
    inside_circle = 0
    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if math.sqrt(x**2 + y**2) <= 1:
            inside_circle += 1
    return 4 * inside_circle / points


def multip_pi_Monte_Karlo(points: int, cores: int = 6):
    with ThreadPoolExecutor(cores) as pool:
        results = pool.map(pi_Monte_Karlo, [points // cores] * cores)
    return sum(results) / cores


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Example 1')
    parser.add_argument('-p', '--number_points',
                        type = int,
                        default = 100000
                        )
    args = parser.parse_args()
    logging.info(multip_pi_Monte_Karlo(args.number_points))
    logging.info(time() - start )
