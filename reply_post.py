#!/usr/bin/python

# This script searches the subreddit r/PythonforEngineers for
# the last 5 submissions in the hot filter with
# "I love Python" in the title (not case sensitive),
# then replies to them saying 'Good for you!'.
# IDs of the posts replied to are saved to the
# posts_replied_to.txt file

import praw
import pdb
import re
import os

# Creating the Reddit instance
reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        # read file
        posts_replied_to = f.read()
        # split on new line
        posts_replied_to = posts_replied_to.split("\n")
        # remove empty values, converts back to list
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Biddy bot says: Good for you!")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)
            with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")
