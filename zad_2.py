"""Module providing a function printing python version 3.11.5."""
import logging
import argparse
import numpy
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(level=logging.DEBUG)


def sum_elem_matrix(num_columns: int, num_raws: int, matrix: list):
    if len(matrix) != num_columns * num_raws:
        raise IndexError("size is not matrix size") 
    high = max(num_columns, num_raws)
    lists = numpy.array_split(matrix, high)
    with ThreadPoolExecutor(high) as executor:
        result = executor.map(sum, lists)
    return sum(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Example 1')
    parser.add_argument('-c', '--num_columns',
                        type = int,
                        default = 3
                        )
    parser.add_argument('-r', '--num_raws',
                        type = int,
                        default = 4
                        )
    parser.add_argument('-m', '--items_matrix',
                        type = list,
                        default = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                        )
    args = parser.parse_args()
    res = sum_elem_matrix(args.num_columns, args.num_raws, args.items_matrix)
    logging.info(res)
