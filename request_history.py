import re


def save_requests(submission):
    regex_match = "(?<=[/])(?<=[r][/])([a-zA-Z0-9\_]+)"
    with open('requests.txt', 'r+') as f:
        for top_level_comment in submission.comments:
            match = re.findall(regex_match, top_level_comment.body)

            for request in match:
                found_request = any(request in line for line in f)
                if not found_request:
                    f.write(request + "\n")
                    print("Recorded request: " + request)
                else:
                    pass
        f.close()
