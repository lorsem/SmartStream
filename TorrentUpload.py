#!/usr/bin/env python

import cgi
import os
import cgitb
import time

cgitb.enable()


# Generator to buffer file chunks

start = time.time()
uploadFlag = 0
form = cgi.FieldStorage()
message = str()
# A nested FieldStorage instance holds the file
#fileitem = form['file']
for n in range(100):
    try:
        fileitem = form['file'][n] #USE THIS says reddit form['file'].fil
    except TypeError:
        if uploadFlag == 0:
            uploadFlag = 1
            fileitem = form['file']
        else:
            break
    except:
        break
    if fileitem.filename:
        # strip leading path from file name to avoid directory traversal attacks
        fn = os.path.basename(fileitem.filename)
        with open( '/home/pi/NewTorrents/' + fn , 'wb') as wfile:
            wfile.write(fileitem.file.read())
        message += 'Upload {} Successful! <br>'.format(n+1)
    else:
        message += 'Upload {} failed! :-(<br>'.format(n+1)
end = time.time()
print "Content-Type: text/html; charset=UTF-8"
print """
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
<title>SmartStream : Uploader</title>
</head>
<body>
<a href="/">
        <img src="/wallpapers/Logo.png" alt="SmartStream" /></a>
                <div id="logo">
                </div>
<br><center><font color="White" size="4"> 
{0}
<br></font>
</center>
<br>
<br>
<center>
<font color="White" size="5">
<a href="http://192.168.1.150/index.html"><b>HOME</b></a>
</font><font color="White" size = "3">
<br> Uploading took {1} seconds
</font>
</center>
</center>
<br>
<br>
</body>
</html>

""".format(message,  end-start)
