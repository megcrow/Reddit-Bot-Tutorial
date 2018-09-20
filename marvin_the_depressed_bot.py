#!/usr/bin/python

import praw
import re
import random
import time
import sys

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("pythonforengineers")
marvin_quotes = []


""" Searches through recent comments for 'Marvin Help' and replies.
Stops after 5 requests that result in no new items """
for comment in subreddit.stream.comments(pause_after=5):
    if comment is None:
        break
    with open("marvin_quotes.txt", "r") as f:
        marvin_quotes = f.read()
        marvin_quotes = marvin_quotes.split("\n")
        marvin_quotes = list(filter(lambda x: False if len(x) == 0 or
                             x[0] == "#" else True, marvin_quotes))
    if re.search("Marvin Help", comment.body, re.IGNORECASE):
        marvin_reply = "Marvin the Depressed Robot says: " \
                     + random.choice(marvin_quotes)
        comment.reply(marvin_reply)
        print(marvin_reply)
    print random.choice(marvin_quotes)
