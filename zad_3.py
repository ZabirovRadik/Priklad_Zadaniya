"""Module providing a function printing python version 3.11.5."""
import logging
import argparse
from multiprocessing import Pool


logging.basicConfig(level=logging.DEBUG)


def find_word(word: str, file_name: str):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                if word in line:
                    return file_name
    except FileNotFoundError as e:
        logging.error(e)
    


def find_word_files(key_word: str, list_of_files: list, cores: int = 6) -> list:
    results = []
    with Pool(cores) as p:
        for file_name in list_of_files:
            result = p.apply_async(find_word, (key_word, file_name))
            results.append(result.get())
    return list(filter(lambda a: a != None, results))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Example 1')
    parser.add_argument('-w', '--key_word',
                        type = str,
                        default = "URL"
                        )
    parser.add_argument('-f', '--list_of_files',
                        type = list,
                        default = ["example", "empty"]
                        )
    args = parser.parse_args()
    res = find_word_files(args.key_word, args.list_of_files)
    logging.info(res)
