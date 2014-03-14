#!/usr/bin/python
import cgi
import cgitb
import os
cgitb.enable()
import os

def isMovie(filename):
    """
    If it is a movie it returns the filename without the extension (to be used in index file)
    else return False
    """
    videoExtensions = ('.wmv', '.mov', '.mpg', '.avi', '.mp4', '.mkv', 'm4v', '.flv') # Tuple containing supported video extensions
    if filename.endswith(videoExtensions):
        return os.path.splitext(filename)[0] # splitext return a list: [name, extension] 
    else: return False

def getIndex(directory):
    """
    os.walk() is awesome. Nothing more to say...
    The tupla returned gets unpaked, files contains filenames while root contains the filepath from passed
    argument to dile diretctory.
    It returns a dictionary, key = file name without extension, value = full file path with extension
    """
    index = {}

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            name = isMovie(filename) # False if not a movie
            if  name:    
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                relFilePath = os.path.relpath(filepath, directory) # relpath returns releative path of first argument
                index[name] = relFilePath  # Adds new item to dictionary

    return index  





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


