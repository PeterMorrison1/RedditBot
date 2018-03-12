import praw
from history import save_requests
from imagehandler import download_image


def authenticate():
    # Requires the praw.ini file, the format can be found at https://praw.readthedocs.io/en/latest/index.html
    reddit = praw.Reddit('Binger_Bot', user_agent='script: reddit_binge_bot:v0.1 (by /u/Binger_Bot)')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit


def fetch_requests(reddit):
    # Finds subreddit strings in the top-most level comments (ex: '/r/subredditname')
    subreddit = reddit.submission(url='https://www.reddit.com/r/RedditBinge/comments/6us5kk/'
                                       'comment_in_this_thread_to_request_a_subreddit_to/')
    save_requests(subreddit)


def top_post_urls(reddit, subreddit):
    # uses praw to take the url of the top posts in a subreddit to download
    # could use imgur api to download imgur specific submissions, HOWEVER, it costs api credits, so crawling it is...

    # number of posts to download is set by .top(limit=#). 5 is currently used for testing. Limit will be higher later
    count = 1
    for submission in reddit.subreddit(subreddit).top(limit=5):
        title = submission.title
        url = submission.url

        # skips imgur links that have a removed image. Needs work, still downloads some
        if "removed" in url:
            print("Image was removed from imgur from post:" + title + "\n")
            pass
        elif submission.is_self or submission.is_video:
            print("This is a self post or video, skipping...")
            pass
        else:
            # count is to name the file, 1.jpg, 2.gif, 3.jpg, etc...
            download_image(url, subreddit, title, count)
        count += 1
