import os


def upload(client, album, subreddit_name, file_name, post_title):
    # set file path to directory that stores images (TBD when moved to raspberry pi) file name for download
    file_path = os.path.join('C:\\Users\\Peter\\Desktop\\' + subreddit_name + '\\' + file_name)

    # imgur has a 129 character limit for titles, but descriptions are longer. So title is stored in description
    config = {
        'album': album['id'],
        'description': post_title
    }

    # uploads file specified in file_path to imgur under the album for the subreddit
    if 'gifv' in file_name or 'mp4' in file_name or 'gfycat' in file_name:
        print("Passing because wrong extension")
        pass
    else:
        client.upload_from_path(file_path, config=config, anon=False)
        print("Done uploading")


def create_album(client, title):
    # creates an album with the title of the subreddit that was scraped
    fields = {
        'title': title
    }
    album = client.create_album(fields=fields)
    return album


def get_album_url(client):
    # gets the album url from the album id. Ends after finding most recent
    for album in client.get_account_albums('me'):
        album_title = album.title if album.title else 'Untitled'
        album_url = "https://imgur.com/a/" + album.id
        print("Album: {0} ({1}) {2}".format(album_title, album.id, album_url))

        # album url will be returned, which will be posted to /r/RedditBinge
        return album_url
