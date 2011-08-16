#! /bin/sh

#
# Modified ever so slightly from a script for the Astronomy Pic of the Day
# wallpaper switcher
# made by Harold Bakker, harold@haroldbakker.com
# http://www.haroldbakker.com/
#

/usr/bin/osascript <<END
tell application "Finder"
	set pFile to POSIX file {"$1"} as string
	set desktop picture to file pFile
	end tell
END