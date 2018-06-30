# RedditBot

This project is a bot that is used to read user inputs from a reddit thread on reddit.com/r/RedditBinge,
the inputs being requests for subreddits to be re-uploaded onto /r/RedditBinge in a single album per subreddit
for easier viewing. The future plans after the base features are complete is still unknown, but it will continue 
to be updated.

I hope someone finds this bot to be useful!

Unfortunately gifv and mp4 aren't supported formats in the free imgur api, so they are excluded from the project after
March 11, 2018. 

# Tools/Libraries/etc Used

These are the main tools/libraries/etc used in the project, all of which have a link provided just in case anyone needs
one. This doesn't include all tools/libs/etc, just main ones that aren't included in base python.

This uses PRAW to crawl reddit for comments/requests of subreddits. PRAW is also used to post the albums on RedditBinge.
https://github.com/praw-dev/praw

Requests is used to download images from common reddit image/gif hosting websites.
http://docs.python-requests.org/en/master/

Beautiful Soup 4 is also used for finding image sources on pesky websites or from posts where the image isn't directly
posted. https://www.crummy.com/software/BeautifulSoup/

Imgur api is used to gain refresh and access tokens for use in ImgurPython. https://apidocs.imgur.com/

ImgurPython is used to upload images. https://github.com/Imgur/imgurpython

# Update

This was originally intended to be a quick script but issues came up that I wasn't expecting. I plan to rework this script
after my current project (Open-Podcast and possibly another small project before that). The rework will simply download the
top N images from the entered subreddit when running the script, rather than re-upload them. The next version/rework won't require a reddit account!

# How to run

To run the script you must have a "praw.ini" file in your main directory of the project with this text in it then hit run:

[Binger_Bot]

username: [Insert reddit username]

password: [Insert reddit password]

client_id: [Insert reddit client id]

client_secret: [Insert reddit client secret]



# Developer/Project info
The project is made by The-Canuck


The repository is found here: https://github.com/The-Canuck/RedditBot
