# RedditBot

This project is a bot that is used to read user inputs from a reddit thread on reddit.com/r/RedditBinge,
the inputs being requests for subreddits to be re-uploaded onto /r/RedditBinge in a single album per subreddit
for easier viewing. The future plans after the base features are complete is still unknown, but it will continue 
to be updated.

I hope someone finds this bot to be useful!

# Tools/Libraries/etc Used

These are the main tools/libraries/etc used in the project, all of which have a link provided just in case anyone needs
one. This doesn't include all tools/libs/etc, just main ones that aren't included in base python.

This uses PRAW to crawl reddit for comments/requests of subreddits. PRAW is also used to post the albums on RedditBinge.
https://github.com/praw-dev/praw

Requests is used to download images from common reddit image/gif hosting websites.
http://docs.python-requests.org/en/master/

Beautiful Soup 4 is also used for finding image sources on pesky websites or from posts where the image isn't directly
posted. https://www.crummy.com/software/BeautifulSoup/

Imgur api is utilized to upload the images into albums onto imgur (Next to be implemented). https://apidocs.imgur.com/

# Developer/Project info
The project is made by The-Canuck


The repository is found here: https://github.com/The-Canuck/RedditBot
