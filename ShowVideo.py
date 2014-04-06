#!/usr/bin/python
'''
Given a relative path (relative to the root of the website), the video is nicely
embedded in HTML5. The VidName is needed only to have a better output.
'''
import cgi
import cgitb

cgitb.enable()

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
            <video width="1280" height="720" controls autoplay poster="/wallpapers/loading.gif">
                <source src="{1}">
            </video>
        </center>

        <br>
    </body>
</html>
'''.format(VidName,  Path)  # Double curled braces to escape python :)  'http://192.168.1.150' +
