import os

def isMovie(filename):
    videoExtensions = ('.wmv', '.mov', '.mpg', '.avi', '.mp4', '.mkv', 'm4v', '.flv')
    if filename.endswith(videoExtensions):
        return True
    else: return False

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    Movie files will be selected and listed.
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


