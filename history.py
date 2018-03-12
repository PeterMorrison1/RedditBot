import re


# save requested subreddits in text file for future use since imgur has a daily limit of uploads
def save_requests(subreddit):
    regex_match = "(?<=[/])(?<=[r][/])([a-zA-Z0-9\_]+)"

    with open('requests.txt', 'r+') as f:
        # find all subreddits mentioned in comments and save them
        for top_level_comment in subreddit.comments:
            match = re.findall(regex_match, top_level_comment.body)

            for request in match:
                # prevent duplicate subreddits from occurring
                found_request = any(request in line for line in f)
                if not found_request:
                    f.write(request + "\n")
                    print("Recorded request: " + request)
                else:
                    pass


def read_post_title(file_path):
    # reads and returns the post titles from titles.txt in a subreddit folder as a list
    with open(file_path, 'r') as f:
        post_title = f.readlines()
    return post_title


def save_finished_requests(subreddit):
    # keeps record of subreddits that have been downloaded
    with open('finished_requests.txt', 'a') as f:
        f.write(subreddit + "\n")


# returns a subreddit to be downloaded, if it hasn't already been downloaded
# cross references 'requests.txt' and 'finished_requests.txt' to determine what has already been downloaded
def next_subreddit():
    # get list of subreddits already downloaded
    with open('finished_requests.txt', 'r') as f:
        finished_sub = f.read()

    # returns request of lines in 'requests.txt' that doesn't match any lines in finished_'finished_requests.txt'
    with open('requests.txt', 'r') as f:
        for request in (line.strip() for line in f):
            if request not in finished_sub:
                print("No match: " + request)
                save_finished_requests(request)
                return request
            else:
                print("Match: " + request)
        print("\n")
