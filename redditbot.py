import praw
import time
import imagehandler
import request_history


def authenticate():
    # Requires the praw.ini file, the format can be found at https://praw.readthedocs.io/en/latest/index.html
    reddit = praw.Reddit('Binger_Bot', user_agent='script: reddit_binge_bot:v0.1 (by /u/Binger_Bot)')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit


def fetch_requests(reddit):
    # Finds subreddit strings in the top-most level comments (ex: '/r/subredditname')
    submission = reddit.submission(url='https://www.reddit.com/r/RedditBinge/comments/6us5kk/'
                                       'comment_in_this_thread_to_request_a_subreddit_to/')
    request_history.save_requests(submission)


def main():
    url = "https://i.redd.it/y8mhykcsdeh01.jpg"  # test var
    subreddit = "aww"  # test var
    title = "test"  # test var
    # test vars above will be removed when reading directly from subreddit is implemented

    reddit = authenticate()
    while True:
        fetch_requests(reddit)
        # skips imgur links that have a removed image
        if "removed" in url:
            print("Image was removed from imgur from post:" + title + "\n")
            pass
        else:
            imagehandler.download_image(url, subreddit, title)
        time.sleep(60)


if __name__ == "__main__":
    main()

