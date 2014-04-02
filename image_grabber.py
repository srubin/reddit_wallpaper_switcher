#! /usr/bin/python
# Reddit Wallpaper Switcher
# Copyright 2011-2013 Steven Rubin - nerdforlife@gmail.com
#Permission is hereby granted, free of charge, to any person obtaining
#a copy of this software and associated documentation files (the
#"Software"), to deal in the Software without restriction, including
#without limitation the rights to use, copy, modify, merge, publish,
#distribute, sublicense, and/or sell copies of the Software, and to
#permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
#LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
#WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# set subreddit.
# suggestions: aww, earthporn, animalporn, cityporn
PICTURES_SUBREDDIT = "earthporn"

# set directory to store pics (relative to image_grabber.py)
PICS_DIRECTORY = "images/"

import os
import sys
import subprocess
from urllib import urlretrieve

import praw


def get_top_image():
    r = praw.Reddit(user_agent="reddit_wallpaper_switcher")
    stories = r.get_subreddit(PICTURES_SUBREDDIT).get_hot(limit=5)
    pic_dir = os.path.join(os.getcwd(), PICS_DIRECTORY)

    for story in stories:
        if story.url.endswith(".jpg"):
            url = story.url
            break
    else:
        exit()

    outpath = os.path.join(pic_dir, url.split("/")[-1])

    print url, outpath

    urlretrieve(url, outpath)
    return outpath


def set_wallpaper(path):
    subprocess.Popen("sh setwp.sh \"{}\"".format(path), shell=True)


def main():
    set_wallpaper(get_top_image())


if __name__ == '__main__':
    main()
