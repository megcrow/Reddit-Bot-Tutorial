#!/usr/bin/python

import praw

SUPPORTED_FILTERS = ["new", "hot", "controversial", "top", "quit"]

reddit = praw.Reddit('bot1')


def get_sub_info(submission):
    print "Title: ", submission.title, "\n"
    print "Author: ", submission.author, "\n"
    if submission.selftext:
        print "Text: ", submission.selftext, "\n"
    print "Score: ", submission.score, "\n"
    print("---------------------------------\n")


def get_filter():
    try:
        if filter == "hot":
            for submission in subreddit.hot(limit=5):
                get_sub_info(submission)

        if filter == "new":
            for submission in subreddit.new(limit=5):
                get_sub_info(submission)

        if filter == "top":
            for submission in subreddit.hot(limit=5):
                get_sub_info(submission)

        if filter == "controversial":
            for submission in subreddit.hot(limit=5):
                get_sub_info(submission)
    except:
        print ("\nInvalid subreddit name. Could not fetch results.")


while True:
    sub = raw_input(("\nWhich subreddit would you like to see?"
                     " Enter 'quit' to exit. ")).lower()
    subreddit = reddit.subreddit(sub)

    if sub == "quit":
        break

    filter = raw_input("\nEnter the filter for the subreddit posts.").lower()

    if filter not in SUPPORTED_FILTERS:
        print(("\nFilter input unsupported. Please input new, hot,"
              " controversial, or top. Type 'quit' to exit. "))

    if filter in SUPPORTED_FILTERS:
        get_filter()
