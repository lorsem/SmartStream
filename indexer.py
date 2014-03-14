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

def getIndex(scanDir, refDir):
    """
    os.walk() is awesome. Nothing more to say...
    The tuple returned gets unpaked, files contains filenames while root contains the absolute filepath from passed
    argument to the file's diretctory.
    The Function returns a dictionary, key = file name without extension, value = full file path with extension, relative to refDir
    """
    index = {}

    # Walk the tree.
    for root, directories, files in os.walk(scanDir):
        for filename in files:
            name = isMovie(filename) # False if not a movie, else movie-name
            if  name:    
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                # Get relative path of file and add it to dictionary. Relpath returns relative path of first argument based on second argument
                index[name] =  os.path.relpath(filepath, refDir) # Adds new item to dictionary: key = movie-name, value = movie's relative path
    return index  

def printIndex(index):
    sortedKeys = sorted(index.keys()) # A list of sorted keys
    with open('./index.txt', 'w') as f:
        for key in sortedKeys:
            f.write('{} {}\n'.format(key, index[key]) # Python converts \n to os.linesep
    f.close() # Just in case...



