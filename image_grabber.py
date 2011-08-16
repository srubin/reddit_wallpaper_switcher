#! /usr/bin/python
# Reddit Wallpaper Switcher 
# (c) 2011 Steve Rubin - nerdforlife@gmail.com

# Set subreddit and local folder to store pictures
PICTURES_SUBREDDIT = "earthporn"
PICS_DIRECTORY = "images/"
CODE_PATH = "/Users/srubin/code/reddit_wallpaper_switcher/"

import reddit
from urllib import urlretrieve
import os
import sys
import subprocess

r = reddit.Reddit(user_agent="reddit_wallpaper_switcher")
stories = r.get_subreddit(PICTURES_SUBREDDIT).get_hot(limit=5)
url = ""
     
for story in stories:
    if story.url.endswith(".jpg"):
        url = story.url
        break
if url == "":
    exit()

outpath = os.path.join(CODE_PATH + PICS_DIRECTORY, url.split("/")[-1])
urlretrieve(url, outpath)

subprocess.Popen("sh " + CODE_PATH + "setwp.sh " + outpath, shell=True)
