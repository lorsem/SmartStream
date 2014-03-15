#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import indexer

# Retrieve form fields
form = cgi.FieldStorage()			# Get POST data
scanDir = form.getfirst("scanDir")			# Pull fname field data
Index = open('/var/www/list_of_films.txt', 'w')
if scanDir is None:
    scanDir = '/var/www'
refDir = '/var/www'
TheDir = indexer.getIndex(scanDir, refDir)
total = indexer.printIndex(TheDir)
#output on the page of the script
print "Content-Type: text/html; charset=UTF-8"
print ''
print '''
<html>
<body>
Indexing completed! <br>
Found <b>{0}</b> films!
<br>
Searched <b>{1}</b>
<br>
<a href="http://192.168.1.150/index.html"><b>HOME</b></a>
<br><br>
{2}
</body>
</html>
'''.format(str(total), scanDir, TheDir)
