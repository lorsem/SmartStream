#!/usr/bin/env python

import cgi   # The file is uploaded through a POST form (see
             #  "TorrentUploadInterface.html" for an example)
import os
import cgitb 
import time  # Used for measuring time passed from beginning of execution

cgitb.enable()


start = time.time() 
uploadFlag = 0  # See below (for loop->try statement);its sole purpose is to try
                #   and upload a single file only once. If the user uploads more
                #   than a single file, files are in an array/list and the
                #   IndexError exception is caught (for loop->except). If there
                #   is just one file, TypeError exception is raised and the file
                #   must be uploaded just once
form = cgi.FieldStorage()
message = str()
# A nested FieldStorage instance holds the file
#fileitem = form['file']
for n in range(100):
    try:
        fileitem = form['file'][n] #USE THIS says reddit form['file'].fil
    except TypeError:  # Happens if we have a single file instead of multiple files.
                       # If there is only one file -> no array, but single file descriptor
        if uploadFlag == 0: # We have only one file. Is it the 1st time we copy it to the disk?
            uploadFlag = 1  # Set the flag, we have our file and will copy it later on
            fileitem = form['file']
        else:       # We have already uploaded our file
            break
    except: # We had multiple files and have copied them all on disk, or something bad happened..
        break
    if fileitem.filename: # Check if file is not None
        # strip leading path from file name to avoid directory traversal attacks
        fn = os.path.basename(fileitem.filename) # Filename variable: complete path
        with open( '/home/pi/NewTorrents/' + fn , 'wb') as wfile:
            wfile.write(fileitem.file.read())
    # A message will be printed to inform user of successful/unsuccessful uploads
        message += 'Upload {} Successful! <br>'.format(n+1) 
    else:
        message += 'Upload {} failed! :-(<br>'.format(n+1)
end = time.time()  # Stop counting and render the page!
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
<a href="/index.html"><b>HOME</b></a>
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
