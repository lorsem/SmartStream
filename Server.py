#!/usr/bin/env python

from __future__ import print_function
import cgi
import time
import cgitb
import indexer  # Actual indexing and sorting
import CreateFilmIndex  # Creation of index.html page (on server)

# This program is the core of the "search+index files" part
# See index.html for an example
start = time.time()
cgitb.enable()                       # Retrieve form fields
form = cgi.FieldStorage()	     # Get POST data
scanDir = form.getfirst("scanDir")   # Pull scanDir: the directory that will be searched for media files
Index = open('/var/www/list_of_films.txt', 'w')
if scanDir is None: # If it is None, nothing has been inserted by the user, which stands for default
    scanDir = '/var/www/video'
refDir = '/var/www' # The files MUST be in a subdirectory of the website.
# The root of the website is /var/www, hence it is the "starting point" of every link
TheIndex = indexer.getIndex(scanDir, refDir) # Returns a dictionary {directory : { name : path}}
total = indexer.CountFiles(TheIndex)    # Counts how many films we have found
CreateFilmIndex.IndexEverything(TheIndex)   # Creates index.html
end = time.time()
print ("Content-Type: text/html; charset=UTF-8")
# NOTE: in following css I used double '{' to escape them since I also use {} for
# .format method!
print ('''
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/PageStyle.css" />
    <style type="text/css">
        a:link {{
        color : white ;
        background-color:transparent;
        text-decoration:none;     /* no underline */
    }}
    a:visited {{
        color : white ;
        background-color:transparent;
        text-decoration:none;     /* no underline */
    }}
    a:hover {{
        color : white ;
        background-color:transparent;
        text-decoration:none;     /* no underline */
    }}
    a:active {{
        color : white ;
        background-color:transparent;
        text-decoration:none;
    }}
    </style>
    <link rel="SHORTCUT ICON" HREF="/wallpapers/icon_small.png">
<title>SmartStream : Indexer</title>
</head>
<body>
<a href="/">
        <img src="/wallpapers/Logo.png" alt="SmartStream" /></a>
                <div id="logo">
                </div>
<br><center><font color="White" size="4">Indexing completed!  <br>
Found <b>{0}</b> films!
<br></font><font color="#FFFFFF" size="3">
Searched <b>{1}</b></font></center>
<br>
<br>
<center>
<font color="White" size="5">
<a href="/index.html"><b>HOME</b></a>
</font><font color="White" size = "3">
<br> Indexing took {2} seconds
</font>
</center>
<br>
</body>
</html>
'''.format(str(total), scanDir, end-start))  # TheIndex
