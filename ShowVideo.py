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
                <title>SmartStream: {0}</title>
                </head>
                <body>
                <center>File: {0}</center>
                
                <video width="1920" height="1080" controls autoplay>
                  <source src="{1}">
                </video>
                <br><br>
                <a href="/FilmIndex.html">Film Index</a>
                <br>
                </body>
                </html>
'''.format(VidName, 'http://192.168.1.150' + Path)
