#!/usr/bin/python
'''
Given a relative path (relative to the root of the website), the video is nicely
embedded in HTML5. The VidName is needed only to have a better output.
'''
import cgi
import cgitb
## Please see also ShowVideo.py

cgitb.enable()
# This version of the ShowVideo uses vlc browser plugin. It works great, if you
# have the plugin. To date (30/04/2014) there is none available for MacOS, which
# I use. On linux (and likely Windows) it should work like a charm (on linux it
# does...).
# This version will soon be used alongside the other one. Choice will be given
# as to which method use: html5 video tag or vlc plugin object

Fields = cgi.FieldStorage()
PartialPath = Fields.getvalue('VidPath')
VidName = Fields.getvalue('VidName')
Path = PartialPath

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
            Video: {0}</font></font>
        </center>
        <center>

    <object type="application/videolan-vlc" data="{1}" width="1280" height="720" id="Video">
         <param name="movie" value="{1}"/>
         <embed type="application/videolan-vlc" name="video1"
         autoplay="no" loop="no" width="1280" height="720"
         target="{1}" />
         <a href="{1}">Download Video1</a>
    </object>

        </center>

        <br>
    </body>
</html>
'''.format(VidName,  Path)  # Double curled braces to escape python :)  'http://192.168.1.150' +





###Stub things below..
#
#
#
#<object type="application/videolan-vlc" data="{1}" width="1280" height="720" id="Video">
#     <param name="movie" value="{1}"/>
#     <embed type="application/videolan-vlc" name="video1"
#     autoplay="no" loop="no" width="1280" height="720"
#     target="{1}" />
#     <a href="{1}">Download Video1</a>
#</object>
