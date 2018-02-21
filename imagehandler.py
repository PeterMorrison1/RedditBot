import requests
import os
from os import path
import bs4


# the url and file path are currently just for testing this works, will be changed next
def download_image(url, subreddit, title, count):
    # get extension from url (gif,mp4,jpg) and turn imgur and gfycat gifs into the proper format
    url, file_extension = url_handler(url)

    # set directory for images to be saved, desktop location is temporary
    file_path = path.join('C:\\Users\\Peter\\Desktop\\', subreddit)

    # creates file path using subreddit, if it doesn't already exist
    try:
        os.makedirs(file_path)
    except FileExistsError:
        pass

    # go to url and save the file to the file path
    response = requests.get(url)
    try:
        # if there is an invalid response code then an exception is raised (ex: 404 code)
        response.raise_for_status()
        # save file, title of the file is top post order, title is saved in a file below
        with open(file_path + "\\" + str(count) + "." + file_extension, 'wb') as f:
            f.write(response.content)
            f.close()
        print("Successful download!")
        # saves the title of the post for uploading on imgur
        with open(file_path + "\\titles.txt", 'a') as f:
            f.write(title + "\n")
            f.close()

    except requests.exceptions.HTTPError as e:
        print(str(e))
    except FileNotFoundError:
        print("Directory does not exist")


def url_handler(url):
    # splits url to get file extension
    file_extension = ""
    url = fetch_image_url(url)

    # gfycat has a unique format, so it must be handled first
    if "gfycat" in url:
        file_extension = "mp4"
        url_split = url.split('/')
        url = url.replace(url_split[2], "thumbs." + url_split[2])
        url += "-mobile." + file_extension
        return url, file_extension

    # imgur uses .gif in url, but thats just for show, must convert to .mp4 to save it properly
    try:
        url_split = url.split('.')
        file_extension = url_split[-1]
        if url_split[1] == "imgur" and (file_extension == "gif" or file_extension == "gifv"):
            file_extension = "mp4"
            url = url.replace(url_split[-1], file_extension)
            return url, file_extension
    except UnboundLocalError:
        print("Unsupported url: " + url)

    return url, file_extension


def fetch_image_url(url):
    supported_formats = (".gif", ".gifv", ".png", ".jpg", ".mp4")

    # checks if the url is to the source image or not, if not it finds the source image
    if not url.endswith(supported_formats):
        response = requests.get(url).content
        soup = bs4.BeautifulSoup(response, "html.parser")
        url_split_slash = url.split('/')

        # loops through all image sources in HTML and sets the correct image url
        images = soup.findAll('img')
        for image in images:
            # imgur links in the HTML are missing the http: so don't remove this
            if "imgur" in image['src']:
                url = "http:" + image['src']
                break
            # this statement looks for matching urls endings between the source and container url
            # ex) The container url: 'http://www.livememe.com/apbp6e9'. The ending: 'apbp6e9'
            elif url_split_slash[-1] in image['src']:
                url = image['src']
            else:
                continue
    return url
