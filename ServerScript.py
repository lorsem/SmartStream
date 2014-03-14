#!/usr/bin/python
import cgi
import cgitb
import os
cgitb.enable()
import os
import indexer



# Retrieve form fields
form   = cgi.FieldStorage()			# Get POST data
scanDir  = form.getfirst("scanDir")			# Pull fname field data
Index = open('/var/www/list_of_films.txt', 'w')
if scanDir == None:
    scanDir = '/media/HDD'
refDir = '/var/www'
DirList = indexer.getIndex(scanDir, refDir)
pos = 0
while True:
    try:
        Index.write(DirList[pos])
        Index.write('\n') #NEEDED!
    except IndexError:
        break
    pos += 1
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
</body>
</html>
'''.format(str(pos), scanDir)


