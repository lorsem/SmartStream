#!/usr/bin/env python

import os
import pickle
import difflib

def isMovie(filename):
    """
If it is a movie it returns the filename without the extension
(to be used in index file) else returns False
    """
    videoExtensions = ('.wmv', '.mov', '.mpg', '.avi', '.mp4', '.mkv', 'm4v',
                       '.flv')  # Tuple containing supported video extensions
    # os.path.splitext() splits a string separating a .extension
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

def prettifyName(elems): ######NOT WORKING!!! Work in progress!
    temp = None
    commonParts = list()
    for key in elems.iterkeys():
        if key.startswith('.') | (key == 'lost+found'):
            continue
        if type(key) is dict:
            prettifyName(key)
            continue
        elif not (type(key) is dict):
            if not isMovie(key):
                continue
            if temp is None:
                temp = key
                continue
            elif temp != key:
                temp, key = temp.replace('.', ' ') , key.replace('.', ' ')
                commonParts = [x.replace(' ', '') for x in difflib.Differ().compare(temp.split(' '), key.split(' ')) if ( (x[0]!='+') & (x[0] != '-'))]
            newkey = key[:]
            for x in commonParts:
                newkey = newkey.replace(x, '')
            while newkey[0] == ' ':
                newkey = newkey[1:]
            elems[newkey] = elems[key]
            del elems[key]
        #else:
        #    newkey = temp[:]
        #    for x in commonParts:
        #        newkey = newkey.replace(x, '')
        #    try:
        #        elems[newkey.replace(' ', '', 1)] = elems.pop(temp)
        #    except:
        #        pass
                


def getIndex(scanDir, refDir):
    """
os.walk() is awesome. Nothing more to say...
The tuple returned gets unpacked, files contains filenames while root contains
the absolute filepath from passed argument to the file's diretctory.
The Function returns a dictionary, key = file name without extension, value = \
full file path with extension, relative to refDir

DIR LISTING:
    os.dirlist(d) retruns a list of what is in d. Just names. Since we need to know what is a directory 
    and what's not we call os.path.isdir(d) where d MUST be a path, not just the name of a directory.
    
    dirDict is a dictionary: key = name, value = abs path
    
    Dictionary: {folder1 : { folder2 { filmname : filmpath, filmname2 : filmpath2 } } }


    """
    index = {}
    # dirDict is a dictionary mapping names of elements in scanDir to abs path
    dirDict = {key : os.path.join(scanDir, key) for key in os.listdir(scanDir)}
#######    prettifyName(dirDict) #NOT WORKING - disable to test
    for elem in dirDict.iterkeys():
        if elem.startswith('.'):
            continue
        if elem == "lost+found":
            continue        
        # name = FALSE if not a movie, movie-name cleaned from extenion if a movie
        name = isMovie(elem)
        if name:
            index[name] = os.path.relpath(dirDict[elem], refDir)
        # if it's a directory... isdir requires the path of the directory, not just it's name...
        elif os.path.isdir(dirDict[elem]):
            # tempIndex is gonna be the subDirectory, we need to use another name rather than "index" not to reassign it
            # and loosing what's so far
            tempIndex = getIndex(dirDict[elem], refDir)
            # only store non-empty direcories
            if tempIndex != {}:
                index[elem] = tempIndex
    return index

def CountFiles(index):
    total = 0
    for key in index.iterkeys(): # A list of sorted keys
        if type(index[key]) is dict:
            total += printIndex(index[key])
        else:
            total += 1
    return total

def printIndex(index): #Old name, kept for campatibility
    return CountFiles(index)
