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


