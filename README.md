# Reddit Bot Tutorial

About
-----

This repository contains the code required to build a Reddit bot according to the tutorial made by shantnu, which can be found [here](http://pythonforengineers.com/build-a-reddit-bot-part-1/)

Shantnu's github for the tutorial can be found [here](https://github.com/shantnu/RedditBot)

A few significant modifications have been made to the base tutorial in bot_read.py (Part 1) and marvin_the_depressed_bot.py (Part 4). In bot_read.py, the subreddit and filter is determined by user input rather than hard-coded and the output has been cleaned up for readability. In marvin_the_depressed_bot.py, Marvin's quotes have been moved to a separate text file which is called within the code and a break condition has been applied so that the program does not run forever without KeyInterrupt. 


To run, install praw first:

```
$ pip install praw
```

Create a reddit bot and add the bot's client_id, client_secret, username, password, and user_agent to praw.ini, which are currently left blank for security reasons.

Then, run bot_read.py, which demonstrates the first part of the tutorial, to view the five latest submissions in the user's choice of subreddit and filter of . The program will prompt the user to provide the name of the subreddit and the filter (hot, new, controversial, top) :

```
$ python bot_read.py
```

reply_post.py demonstrates the second part of the tutorial searches r/PythonforEngineers (created by shantnu) for submissions with "I love Python" in their title and replies "Good for you!" To run:

```
$ python reply_post.py
```

marvin_the_depressed_bot.py demonstrates the final part of the tutorial. Quotes taken from IMDB are randomly selected and used as replies to any submission in r/PythonforEngineers that includes "Marvin help". The program will terminate after 5 requests that return no new instances of "Marvin help". To run:

```
$ python marvin_the_depressed_bot.py
```
