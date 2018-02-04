import requests


# the url and file path are currently just for testing this works, will be changed next
def download_image():
    url = "https://i.redd.it/x6uw5a3qf0e01.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        with open("C:\\Users\\Peter\\Desktop\\test.jpg", 'wb') as f:
            f.write(response.content)


if __name__ == "__main__":
    download_image()