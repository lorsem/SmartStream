import os
import pickle


def isMovie(filename):
    """
If it is a movie it returns the filename without the extension
(to be used in index file) else return False
    """
    videoExtensions = ('.wmv', '.mov', '.mpg', '.avi', '.mp4', '.mkv', 'm4v',
                       '.flv')  # Tuple containing supported video extensions
    name, ext = os.path.splitext(filename)
    if ext in videoExtensions:
        return name
    else:
        return False

def store_index(index):
    try:
        with open("index.pkl", "wb") as output:
            pickle.dump(index, output)
    except IOError:
        return False, "No such file"


def getIndex(scanDir, refDir):
    """
os.walk() is awesome. Nothing more to say...
The tuple returned gets unpacked, files contains filenames while root contains
the absolute filepath from passed argument to the file's diretctory.
The Function returns a dictionary, key = file name without extension, value = \
full file path with extension, relative to refDir
    """
    index = {}
    for file in os.listdir(scanDir).sort():
        if os.path.isdir(file):
            with getIndex(os.path.relpath(file, scanDir), refDir) as dir:
                if dir != {}:
                    index[file] = dir
        elif isMovie(file):
                index[file] = os.path.relpath(file, refDir)
                # Get relative path of file and add it to dictionary.
                # Relpath returns relative path of first argument based
                    #on second argument
                # Adds new item to dictionary:
                    #key = movie-name, value = movie's relative path
    return index


def printIndex(index):
    cwd = os.getcwd()
    textPath = os.path.join(cwd, 'video_index.txt')
    total = 0
    sortedKeys = sorted(index.keys())  # A list of sorted keys
    with open(textPath, 'w') as f:
        for key in sortedKeys:
            if type(index[key]) is dict:
                total += printIndex(index[key])
            else:
                total += 1
            f.write('{} {}\n'.format(key, index[key]))
    return total
