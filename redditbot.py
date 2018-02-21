import time
import redditpraw


def main():
    # url = "https://i.redd.it/y8mhykcsdeh01.jpg"  # test var
    subreddit = "aww"  # test var
    # title = "test"  # test var
    # test vars above will be removed when reading directly from subreddit is implemented

    reddit = redditpraw.authenticate()
    while True:
        redditpraw.fetch_requests(reddit)
        redditpraw.top_post_urls(reddit, subreddit)
        time.sleep(60)


if __name__ == "__main__":
    main()
