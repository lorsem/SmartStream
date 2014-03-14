#!/usr/bin/python
import cgi
import cgitb
import os
cgitb.enable()
import os

def isMovie(filename):
    videoExtensions = ('.wmv', '.mov', '.mpg', '.avi', '.mp4', '.mkv', 'm4v', '.flv')
    if filename.endswith(videoExtensions):
        return True
    else: return False

def get_filepaths(directory):
    """
    os.walk() is awesome. Nothing more to say...
    The tupla returned gets unpaked, files contains filenames while root contains the filepath from passed
    argument to dile diretctory.
    Movies are selected and listed with their full filepaht (e.g. directory/subDirectory/movie.extension)
    """
    file_paths = []  # List which will store all of the full filepaths (filename and extension included)

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            if isMovie(filename):    
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.

    return file_paths  






# Retrieve form fields
form   = cgi.FieldStorage()			# Get POST data
TheDirectory  = form.getfirst("TheDirectory")			# Pull fname field data
Index = open('/var/www/list_of_films.txt', 'w')
if TheDirectory.lower() == 'default':
    TheDirectory = '/media/HDD'

DirList = get_filepaths(TheDirectory)
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
'''.format(str(pos), TheDirectory)


