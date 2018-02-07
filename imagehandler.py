import requests
import os
from os import path


# the url and file path are currently just for testing this works, will be changed next
def download_image(url, subreddit, title):
    # set directory for images to be saved, desktop location is temporary
    file_path = path.join('C:\\Users\\Peter\\Desktop\\', subreddit)

    # splits url to get file extension
    try:
        url_split = url.split('.')
        file_extension = url_split[3]
    # gfycat uses different format from other media used on reddit, so this makes it into a requestable url
    except (IndexError):
        if "gfycat" in url:
            file_extension = "mp4"
            url_split = url.split('/')
            url = url.replace(url_split[2], "thumbs." + url_split[2])
            url += "-mobile." + file_extension

    # imgur uses .gif in url, but thats just for show, must convert to .mp4 to save it properly
    if url_split[1] == "imgur" and (file_extension == "gif" or file_extension == "gifv"):
        file_extension = "mp4"
        url = url.replace(url_split[3], file_extension)
    elif url_split[1] == "":
        print("FIX ME, IMGUR URL STUFF")

    # creates file path using subreddit, if it doesn't already exist
    try:
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
        print("Successful download!")
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    except FileNotFoundError:
        return "Directory does not exist"

