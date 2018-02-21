import praw
import history
import imagehandler


def authenticate():
    # Requires the praw.ini file, the format can be found at https://praw.readthedocs.io/en/latest/index.html
    reddit = praw.Reddit('Binger_Bot', user_agent='script: reddit_binge_bot:v0.1 (by /u/Binger_Bot)')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit


def fetch_requests(reddit):
    # Finds subreddit strings in the top-most level comments (ex: '/r/subredditname')
    submission = reddit.submission(url='https://www.reddit.com/r/RedditBinge/comments/6us5kk/'
                                       'comment_in_this_thread_to_request_a_subreddit_to/')
    history.save_requests(submission)


def top_post_urls(reddit, subreddit):
    count = 1
    for submission in reddit.subreddit(subreddit).top(limit=50):
        title = submission.title
        url = submission.url

        # skips imgur links that have a removed image
        if "removed" in url:
            print("Image was removed from imgur from post:" + title + "\n")
            pass
        elif submission.is_self or submission.is_video:
            print("This is a self post or video, skipping...")
            pass
        else:
            imagehandler.download_image(url, subreddit, title, count)
        count += 1
