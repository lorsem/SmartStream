#####import indexer
import difflib
#####STUBB

def RemoveBadSep(wrd):
    for x in ('.', '\n'):  ## Bad separators
        wrd.replace(x, ' ')
    return wrd


def spam(diz): ### NEW idea. It seems not to be working. -.- 
    keysBeingDiz = list()
    keysBeingFiles = list()
    commonParts = list()
    temp = None
    for key in diz.iterkeys():
        if type(diz[key]) is dict:
            keysBeingDiz.append(key)
        else:
            keysBeingFiles.append(key)
    for key in keysBeingDiz:
        spam(diz[key])
    for key in keysBeingFiles:
        oldkey = key[:]
        if temp is None:
            temp = RemoveBadSep(key)
        else:
            key = RemoveBadSep(key)
            for x, y in temp.split(' '), key.split(' '):
                if x == y:
                    commonParts.append(x)
            for x in commonParts:
                key.replace(x, '')
            diz[key] = diz.pop(oldkey)   
        
            
    
            








def makeGoodNames(tree):
    temp = None
    def stripName(name, commons):
        newkey = name[:]
        for x in commons:
            newkey = newkey.replace(x, '')
        while newkey[0] == ' ': ##remove all leading spaces
            newkey = newkey[1:]
        return newkey
    if len(tree) <=1:
        return
    for key in tree.iterkeys():
        if key.startswith('.'):
            continue
        if key == 'lost+found':
            continue
        if temp is None:
            temp = key
            continue
        temp, key = temp.replace('.', ' ').replace('\n', ' ') , key.replace('.', ' ').replace('\n', ' ')
        commonParts = [x.replace(' ', '') for x in difflib.Differ().compare(temp.split(' '), key.split(' ')) if (len(x)>1)&( (x[0]!='+' ) & (x[0] != '-'))]
        print(commonParts)
        if len(commonParts) == 0:
            break
        #print('key: ', key, end='\n')
        try:
            tree[ stripName(key, commonParts) ] = tree.pop(key)
        except:
            pass
    else:
        try:
            tree[ stripName(temp, commonParts) ] = tree.pop(key)
        except:
            pass
        
def prettifyName(elems): ######NOT WORKING!!! Work in progress!
    makeGoodNames(elems)
    for key in elems.iterkeys():
        print('INFOR')
        if type(key) is dict:
            print('ISDICT')
            makeGoodNames(key)
    
    
    
    
### SOON to be deleted - just checking ###
    #temp = None
    #commonParts = list()
    #for key in elems.iterkeys():
    #    if key.startswith('.') | (key == 'lost+found'):
    #        continue
    #    if type(key) is dict:
    #        prettifyName(key)
    #        continue
    #    elif not (type(key) is dict):
    #        if not isMovie(key):
    #            continue
    #        if temp is None:
    #            temp = key
    #            continue
    #        elif temp != key:
    #            temp, key = temp.replace('.', ' ') , key.replace('.', ' ')
    #            commonParts = [x.replace(' ', '') for x in difflib.Differ().compare(temp.split(' '), key.split(' ')) if ( (x[0]!='+') & (x[0] != '-'))]
    #        newkey = key[:]
    #        for x in commonParts:
    #            newkey = newkey.replace(x, '')
    #        while newkey[0] == ' ':
    #            newkey = newkey[1:]
    #        elems[newkey] = elems[key]
    #        del elems[key]
    #    #else:
    #    #    newkey = temp[:]
    #    #    for x in commonParts:
    #    #        newkey = newkey.replace(x, '')
    #    #    try:
    #    #        elems[newkey.replace(' ', '', 1)] = elems.pop(temp)
    #    #    except:
    #    #        pass
  