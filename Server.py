#!/usr/bin/env python
import cgi
import cgitb
import indexer
import CreateFilmIndex

cgitb.enable()
# Retrieve form fields
form = cgi.FieldStorage()			# Get POST data
scanDir = form.getfirst("scanDir")			# Pull fname field data
Index = open('/var/www/list_of_films.txt', 'w')
if scanDir is None:
    scanDir = '/var/www/video'
refDir = '/var/www'
TheIndex = indexer.getIndex(scanDir, refDir)
total = indexer.printIndex(TheIndex)
indexer.store_index(TheIndex) #Quite useless nut not a performance issue
#output on the page of the script

CreateFilmIndex.IndexEverything(TheIndex)


print "Content-Type: text/html; charset=UTF-8"
print ''
print '''
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
        <img src="/wallpapers/Logo.png" alt="SmartStream" />
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
<a href="http://192.168.1.150/index.html"><b>HOME</b></a>
</font>
</center>
<br>
</body>
</html>
'''.format(str(total), scanDir) #TheIndex