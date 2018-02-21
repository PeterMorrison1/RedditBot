import re


# save requested subreddits in text file for future use since imgur has a daily limit of uploads
def save_requests(submission):
    regex_match = "(?<=[/])(?<=[r][/])([a-zA-Z0-9\_]+)"

    with open('requests.txt', 'r+') as f:
        # find all subreddits mentioned in comments and save them
        for top_level_comment in submission.comments:
            match = re.findall(regex_match, top_level_comment.body)

            for request in match:
                # prevent duplicate subreddits from occurring
                found_request = any(request in line for line in f)
                if not found_request:
                    f.write(request + "\n")
                    print("Recorded request: " + request)
                else:
                    pass
        f.close()
