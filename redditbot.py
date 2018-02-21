import time
import imagehandler
import reddit_praw


def main():
    url = "https://i.redd.it/y8mhykcsdeh01.jpg"  # test var
    subreddit = "aww"  # test var
    title = "test"  # test var
    # test vars above will be removed when reading directly from subreddit is implemented

    reddit = reddit_praw.authenticate()
    while True:
        reddit_praw.fetch_requests(reddit)

        # skips imgur links that have a removed image
        if "removed" in url:
            print("Image was removed from imgur from post:" + title + "\n")
            pass
        else:
            imagehandler.download_image(url, subreddit, title)
        time.sleep(60)


if __name__ == "__main__":
    main()
