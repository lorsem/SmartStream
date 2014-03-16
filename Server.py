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
    scanDir = '/var/www/video'
refDir = '/var/www'
TheIndex = indexer.getIndex(scanDir, refDir)
total = indexer.printIndex(TheIndex)
indexer.store_index(TheIndex)
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
<br>
<a href="http://192.168.1.150/cgi-bin/print_list.py"><b>The index (Philippe)</b></a>
<br>
{2}
</body>
</html>
'''.format(str(total), scanDir, 'NULL') #TheIndex
