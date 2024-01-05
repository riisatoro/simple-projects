import os
import requests


def get_extension(image_url: str) -> str:
    available_extensions: list[str] = ['.jpg', '.jpeg', '.png', '.gif', '.svg']
    for extension in available_extensions:
        if extension in image_url:
            return extension

    return None


def download_image(image_url: str, image_name: str) -> None:
    extension: str = get_extension(image_url)
    if not extension:
        raise ValueError(f'Could not get extension from {image_url}')

    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'artifacts', ''.join([image_name, extension]))

    if os.path.isfile(full_path):
        raise FileExistsError(f'Image {image_name} already exists')

    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(full_path, 'wb') as file:
                file.write(response.content)
            print(f'Image was downloaded to {full_path}')
        else:
            print(f'Could not download image from {image_url}')
    except Exception as e:
        print(f'Could not download image from {image_url} - {e}')


def main():
    image_url = input('Enter image URL: ')
    image_name = input('Enter image name: ')
    download_image(image_url, image_name)


if __name__ == '__main__':
    main()
