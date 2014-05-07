#!/usr/bin/python

# Given a relative path (relative to the root of the website), the video is nicely
# embedded in HTML5. The VidName is needed only to have a better output.
#
# NOTE: working also on embedding vlc-plugin object: see ShowVideo_vlc !

import cgi
import cgitb

cgitb.enable()
# Html5-embedded videos are played using the default browser player.
#   It may be a problem: on MacOS, i couldn't find a plugin to play some videos
#   properly (no audio or nothing at all). See bottom of this file and
#   Show__Beta->ShowVideo_vlc for an alternative solution (will soon merge the
#   two of them :) )
Fields = cgi.FieldStorage() # Get data from POST form
# Get the path (/var/www already took away) and the name of the video
PartialPath = Fields.getvalue('VidPath')
VidName = Fields.getvalue('VidName')
Path = PartialPath
# Output html page
print "Content-Type: text/html; charset=UTF-8"
print ''
print '''
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/PageStyle.css" />
        <link rel="SHORTCUT ICON" HREF="wallpapers/icon_small.png">
        <style type="text/css">
            body {{background-color:black;
                    background-image:none}}
        </style>
        <title>SmartStream::Playback</title>
    </head>
    <body>
        <center>
            <a href="/index.html"><font color="#8D8D8D"><font size="4">
            Film Index</font></font></a>
        </center>
        <center>
            <font color="#8D8D8D"><font size="3">
            Video: {vname}</font></font>
        </center>
        <center>
            <video width="1280" height="720" controls poster="/wallpapers/loading.gif">
                <source src="{vpath}">
            </video>
        </center>

        <br>
        <a href="/cgi-bin/ShowVideo_vlc.py?VidPath={vpath}&VidName={vname}">
            <font color="#8D8D8D"><font size="4">
                Open using VLC plugin
            </font></font>
        </a>
    </body>
</html>
'''.format(vname=VidName,  vpath=Path)  # Double curled braces to escape python :)
# See Show__Beta for a vlc-plugin enabled version (works great on linux but not
#   on MacOS). Not tested on windows
