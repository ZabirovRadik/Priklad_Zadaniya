"""Module providing a function printing python version 3.11.5."""
import logging
import argparse
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


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
    


def find_word_files(key_word: str, list_of_files: list) -> list:
    results = []
    with ThreadPoolExecutor(len(list_of_files)) as executor:
        future_to_file = {executor.submit(find_word, key_word, file): file for file in list_of_files}
        for future in concurrent.futures.as_completed(future_to_file):
            try:
                results.append(future.result())
            except Exception as exc:
                print('%r generated an exception: %s' % (future_to_file[future], exc))
    results = list(filter(lambda a: a != None, results))
    return results

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
