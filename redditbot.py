import time
import redditpraw
from history import next_subreddit


def main():
    reddit = redditpraw.authenticate()
    while True:
        redditpraw.fetch_requests(reddit)
        subreddit = next_subreddit()

        # use of break sets the var subreddit as None in history.next_subreddit(), meaning no new subs to download
        if subreddit is not None:
            redditpraw.top_post_urls(reddit, subreddit)
        else:
            print("No new subreddits to binge, sleeping...")
            time.sleep(3600)


if __name__ == "__main__":
    main()
