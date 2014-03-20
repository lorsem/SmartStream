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
   with open( os.path.join('/var/www/video', reldir) , 'wb') as file:
      file.write(fileitem.file.read())
   
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)