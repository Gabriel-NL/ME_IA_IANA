import os
import time
import random
import logging
import requests
from bs4 import BeautifulSoup

# Universal values here

# attempt = 258112622380537764 7388786880085994
link_mold = "/pin/73887868800859"  # "/pin/"
min_value = 90  # 100000000000000000
max_value = 99  # 999999999999999999

max_attempts = 100

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear_console()

logging.basicConfig(filename='pinterest_scraper.log', level=logging.ERROR)

generated_pins = set()
print("[===================================================]")
print("[Trying to find a valid pinterest link, please wait]")
print("[===================================================]")

def generate_random_pinterest_link():
    while True:
        pin_id = random.randint(min_value, max_value)
        pinterest_link = f"https://www.pinterest.com{link_mold}{pin_id}/"

        if pinterest_link not in generated_pins:
            generated_pins.add(pinterest_link)
            return pinterest_link

def is_valid_pinterest_image(link):
    try:
        with requests.Session() as session:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = session.get(link, headers=headers)
            response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error(f"HTTP Error: {errh}")
        return False
    except requests.exceptions.RequestException as err:
        logging.error(f"Request Exception: {err}")
        return False

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        image_element = soup.find('meta', {'property': 'og:image'})
        return image_element is not None and 'content' in image_element.attrs
    except Exception as e:
        logging.error(f"Error parsing HTML: {e}")
        return False

def find_and_print_valid_pinterest_link(attempts=max_attempts):


    for attempt_num in range(1, attempts + 1):
        pinterest_link = generate_random_pinterest_link()
        if is_valid_pinterest_image(pinterest_link):
            print(f"\nValid Pinterest link found after {attempt_num} attempts: {pinterest_link}")
            return pinterest_link

    print(f"\nNo valid Pinterest link found after {attempts} attempts.")


def mass_search_for_Links(attempts):
    links = []
    for i in range(attempts):

        links.append(find_and_print_valid_pinterest_link())
    return links
         


if __name__ == "__main__":
    find_and_print_valid_pinterest_link()
