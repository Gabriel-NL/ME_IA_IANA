import os
import requests
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def download_image_from_url(url, save_filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        return None

    try:
        # Check if the "p_saved" folder exists, create it if not
        save_folder = "p_saved"
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # Determine file extension based on content type
        content_type = response.headers.get('content-type')
        file_extension = content_type.split('/')[-1] if content_type else 'jpg'

        save_path = os.path.join(save_folder, f"{save_filename}.{file_extension}")

        # Download image using urllib and save it to the specified path
        urlretrieve(url, save_path)

        print(f"Image downloaded successfully and saved at {save_path}")
        return save_path
    except Exception as e:
        print(f"Error processing the image: {e}")
        return None

def extract_image_url_from_pinterest(pinterest_url):
    try:
        response = requests.get(pinterest_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the image element on the Pinterest page
    image_element = soup.find('meta', {'property': 'og:image'})

    if image_element and 'content' in image_element.attrs:
        image_url = image_element['content']
        return image_url
    else:
        print("Image URL not found on the Pinterest page.")
        return None

def download_image_from_pinterest(pinterest_url, save_filename):
    image_url = extract_image_url_from_pinterest(pinterest_url)

    if image_url:
        return download_image_from_url(image_url, save_filename)
    else:
        print("Failed to retrieve the image URL.")
        return None

if __name__ == "__main__":
    pinterest_url = input("Enter the Pinterest URL: ")
    save_filename = input("Enter the filename for the saved image: ")

    downloaded_path = download_image_from_pinterest(pinterest_url, save_filename)

    if downloaded_path:
        print(f"Image downloaded and saved at: {downloaded_path}")
    else:
        print("Failed to download the image.")
