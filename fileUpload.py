#!/usr/bin/env python

import cgi
import os
import cgitb
import time

cgitb.enable()


# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
   while True:
      chunk = f.read(chunk_size)
      if not chunk:
         break
      yield chunk

start = time.time()
form = cgi.FieldStorage()
reldir = form.getfirst('dirName')
if reldir is None:
   reldir = ''
# A nested FieldStorage instance holds the file
#fileitem = form['file']
DestDir = 'null'
'''
with form['file'].file as ifile:
   fn = os.path.basename(ifile)
   message = fn
   TargetDir = os.path.join('/var/www/video', reldir)
   try:
      os.makedirs(TargetDir)
   except OSError:
        pass
   DestDir = os.path.join (TargetDir, fn)
   kbytes = 1024 
   wbytes = 1024 * kbytes #Bytes = 1024*1024 = 1 MB
   wfile = open( DestDir  , 'wb', wbytes)
   while True:
      try:
         wfile.write(ifile.read(wbytes) )
      except EOFError:
         message = 'done'
         break
      except Exception as message:
         break
      
   

'''
fileitem = form['file'] #USE THIS says reddit form['file'].file
if fileitem.filename:
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   TargetDir = os.path.join('/var/www/video', reldir)
   try:
      os.makedirs(TargetDir)
   except OSError:
        pass
   DestDir = os.path.join (TargetDir, fn)
   message = ''
   kbytes = 1024
   wbytes = 1024 * kbytes
   wfile = open( DestDir  , 'wb', wbytes)
   for chunk in fbuffer(fileitem.file):
      wfile.write(chunk)
   wfile.close()
   message = 'The file "' + fn + '" was uploaded successfully to' + DestDir 



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
<br><center><font color="White" size="4">Upload completed!  <br>
MSG:{0}
<br></font><font color="#FFFFFF" size="3">
Uploaded to:  <b>{1}</b>
<br></font></center>
<br>
<br>
<center>
<font color="White" size="5">
<a href="http://192.168.1.150/index.html"><b>HOME</b></a>
</font><font color="White" size = "3">
<br> Uploading took {2} seconds
</font>
</center>
</center>
<br>
</body>
</html>

""".format(message, DestDir , end-start)