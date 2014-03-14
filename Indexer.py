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
    The tuple returned gets unpacked, files contains filenames while root contains the filepath from passed
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



