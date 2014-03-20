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
   with open( reldir , 'wb') as file:
      file.write(fileitem.file.read())
   
   message = 'The file "' + fn + '" was uploaded successfully to' + reldir
   
else:
   message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)