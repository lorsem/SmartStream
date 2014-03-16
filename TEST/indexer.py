import os
import pickle


def isMovie(filename):
    """
If it is a movie it returns the filename without the extension
(to be used in index file) else return False
    """
    videoExtensions = ('.wmv', '.mov', '.mpg', '.avi', '.mp4', '.mkv', 'm4v',
                       '.flv')  # Tuple containing supported video extensions
    if filename.endswith(videoExtensions):
        return os.path.splitext(filename)[0]
            # splitext return a list: [name, extension]
    else:
        return False


def store_index(index):
    with open("index.pkl", "wb") as output:
        pickle.dump(index, output)


def getIndex(scanDir, refDir):
    """
os.walk() is awesome. Nothing more to say...
The tuple returned gets unpacked, files contains filenames while root contains
the absolute filepath from passed argument to the file's diretctory.
The Function returns a dictionary, key = file name without extension, value = \
full file path with extension, relative to refDir
    """
    index = {}

    # Walk the tree.
    for root, directories, files in os.walk(scanDir):
        for filename in files:
            name = isMovie(filename)  # False if not a movie, else movie-name
            if name:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                # Get relative path of file and add it to dictionary.
                # Relpath returns relative path of first argument based
                    #on second argument
                index[name] = os.path.relpath(filepath, refDir)
                # Adds new item to dictionary:
                    #key = movie-name, value = movie's relative path
        for directory in directories:
            index[directory] = getIndex(os.path.join(root, directory), refDir)
            if not index[directory]:
                index.pop(directory)
        break
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
                # Python converts \n to os.linesep
        #f.close() # Just in case... Shouldn't be.. ??
    return total