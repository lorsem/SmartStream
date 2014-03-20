#!/usr/bin/env python
import cgi
import os
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
reldir = form.getfirst('dirName')
if reldir is None:
   reldir = ''   
# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   TargetDir = os.path.join('/var/www/video', reldir)
   if not os.path.isdir(TargetDir):
      os.makedirs(TargetDir)
   reldir = os.path.join (TargetDir, fn)
   file = open( reldir , 'wb')
   while True:
      try:
         file.write(fileitem.file.read(2))
      except EOFError:
         message = 'The file "' + fn + '" was uploaded successfully to' + reldir
         break
      except Exception:
         message = 'unknow ERROR'
   



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
<br><center><font color="White" size="4">Upload completed!  <br>
{0}
<br></font><font color="#FFFFFF" size="3">
Uploaded to:  <b>{1}</b></font></center>
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

""".format(message, reldir)