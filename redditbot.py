import time
import redditpraw
import history
import imgurauth
import upload
import os.path


def main():
    # set file path for saved images
    file_path = os.path.join('C:\\Users\\Peter\\Desktop\\')

    while True:
        # create instances of reddit praw and imgur python
        reddit_client = redditpraw.authenticate()
        imgur_client = imgurauth.authenticate()

        # search comments for list of subreddits to process
        redditpraw.fetch_requests(reddit_client)

        # get next subreddit to be downloaded, and uploaded
        subreddit = history.next_subreddit()

        # use of break sets the var subreddit as None in history.next_subreddit(), meaning no new subs to download
        if subreddit is not None:
            redditpraw.top_post_urls(reddit_client, subreddit)
        else:
            pass

        try:
            # checks if a subreddit folder exists, if so then it uploads the contents
            if os.path.isdir(file_path + subreddit):
                album_id = upload.create_album(imgur_client, subreddit)

                # a_url will be passed to a function that will submit the album (a_url) to /r/RedditBinge
                a_url = upload.get_album_url(imgur_client)

                count = 0

                # scans os for each instance of a photo then uploads it and it's title
                for filename in os.listdir(file_path + subreddit):
                    # post_name[count] takes the iteration number and finds corresponding post title
                    post_name = history.read_post_title(file_path + subreddit + '\\titles.txt')

                    # uploads file for this iteration, then adds +1 to count for next post name to match file
                    upload.upload(imgur_client, album_id, subreddit, filename, post_name[count])
                    count += 1

                    # only allowed 50 uploads per hour. So sleep 73 seconds between uploads to avoid cap
                    # its actually 3600/50 = 72. But using 73 here JUST to be careful
                    # this also helps reduce the load on imgur servers
                    time.sleep(73)

        except IndexError:
            # when count goes above the amount of lines in titles.txt
            # another good error!

            print("No more files to upload, passing...")
            pass

        except TypeError:
            # the if condition gets a type error when subreddit is None, which is when there are no more matches
            # so this is a good error!
            print("No new subreddits in the list, passing...")
            pass

        print("No new subreddits to binge, sleeping...")
        time.sleep(3600)


if __name__ == "__main__":
    main()
