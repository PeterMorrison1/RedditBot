import requests
import os
from os import path


# the url and file path are currently just for testing this works, will be changed next
def download_image():
    url = "http://www.freepngimg.com/thumb/reddit/4-2-reddit-png-hd-thumb.png"  # test url
    subreddit = "aww" # test subreddit
    title = "yo" # test title
    # above 3 vars will be added into function call ex: download_image(subreddit, title, url)
    file_path = path.join('C:\\Users\\Peter\\Desktop\\', subreddit)
    url_split = url.split('.', 3)
    file_extension = url_split[3]
    print(url_split)

    # imgur uses .gif in url, but thats just for show, must convert to .mp4 to save it properly
    if url_split[1] == "imgur":
        file_extension = "mp4"
        url = url.replace(url_split[3], file_extension)

    # creates file path using subreddit, and create the file path if it doesn't already exist
    try:
    #if not os.path.exists(file_path):
        os.makedirs(file_path)
    except FileExistsError:
        print("Directory exists already, continuing...")

    # go to url and save the file to the file path
    response = requests.get(url)

    try:
        response.raise_for_status()
        with open(file_path + "\\" + title + "." + file_extension, 'wb') as f:
            f.write(response.content)
            f.close()

    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    except FileNotFoundError:
        return "Directory does not exist"


if __name__ == "__main__":
    download_image()