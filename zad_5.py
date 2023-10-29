"""Module providing a function printing python version 3.11.5."""
import logging
import argparse
import os
import requests
from multiprocessing import Pool


logging.basicConfig(level=logging.DEBUG)


def create_folders(base_folder: str) -> None:
    """Form a folder"""
    if not os.path.exists(base_folder):
            os.mkdir(base_folder)
    

def save_image(url: str, base_folder: str = "dataset") -> None:
    """This func downloads the image from the link"""
    create_folders(base_folder)
    filename = url.split("/")[-1]
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.ok:
            with open(os.path.join(base_folder,filename), 'wb') as file:
                file.write(response.content)
    except Exception as e:
        logging.exception(f"Unable to download image: {url}:{e}")


def download_images(URLs: list):
    with Pool(len(URLs)) as p:
        p.map(save_image, URLs)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Example 1')
    parser.add_argument('-u', '--URLs',
                        type = list,
                        default = ["https://i.pinimg.com/originals/bb/65/95/bb659528f5b2cbf492d4d8df01a9b9b6.png",
                                   "https://noufel1393.gitlab.io/noufel1393/img/blog_images/multiprocessing_vs_multithreading.png"
                                   ]
                        )
    args = parser.parse_args()
    logging.info(download_images(args.URLs))
