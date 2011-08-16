#! /usr/bin/python
# Reddit Wallpaper Switcher 
# (c) 2011 Steve Rubin - nerdforlife@gmail.com

# Set subreddit and local folder to store pictures
PICTURES_SUBREDDIT = "earthporn"
PICS_DIRECTORY = "images/"

import reddit
from urllib import urlretrieve
import os
import sys
import subprocess

r = reddit.Reddit(user_agent="reddit_wallpaper_switcher")
stories = r.get_subreddit(PICTURES_SUBREDDIT).get_top(limit=5)
url = ""
     
for story in stories:
    if story.url.endswith(".jpg"):
        url = story.url
        break
if url == "":
    exit()

outpath = os.path.join(PICS_DIRECTORY, url.split("/")[-1])
urlretrieve(url, outpath)

subprocess.Popen("sh setwp.sh " + outpath, shell=True)
