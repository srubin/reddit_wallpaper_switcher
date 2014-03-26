The Reddit Wallpaper Switcher for Mac OS X will grab the hottest image (.jpg)
in a subreddit, copy it into a local folder, and then set it as the desktop
background image in Mac OS X.

Requires reddit_api python module, which can be found at https://github.com/praw-dev/praw

To select a subreddit, edit the PICTURES_SUBREDDIT variable in [image_grabber.py](image_grabber.py)

To select a local folder, edit the PICS_DIRECTORY variable in [image_grabber.py](image_grabber.py)

To set this up to run every, say, 30 minutes, add the cronjob
```
*/30 * * * * /path/to/image_grabber.py
```

