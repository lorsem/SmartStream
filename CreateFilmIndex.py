#!/usr/bin/env python
'''
Load 'index.pkl' (MUST be in /var/www/cgi-bin) previously created with
indexer.store_index().
Create 'Tree' menu (not really good looking atm), with:
Link to file: pass to ShowVideo.py two arguments: VidPath (RelPath to video)
                                                 and VidName


'''
import pickle
import cgi
import cgitb
cgitb.enable()

def CreateNestedElements(TheFilms, IndexHtml):
    for Name  in TheFilms.iterkeys():
        if type(TheFilms[Name]) == dict:
            IndexHtml.write('''
                            <br>
                            <li>{}
                            <ul>
                            '''.format(Name))
            CreateNestedElements(TheFilms[Name], IndexHtml)
            IndexHtml.write('''
                            </ul>
                            </li>
                            ''')
        else:
            IndexHtml.write('''<br><li><a href = "{0}">{1}</a></li>
                            '''.format('/cgi-bin/ShowVideo.py?VidPath={}&VidName={}'.format('/' + TheFilms[Name], Name),
                                       Name)
                           )
    
def IndexEverything():
    
    Index = open ('index.pkl', 'rb')
    TheFilms = pickle.load(Index)
    
    IndexHtml = open ('/var/www/FilmIndex.html', 'w')
    #head part of page
    IndexHtml.write(
    '''
    <html>
    <head>
    <script type="text/javascript" src="simpletreemenu.js">
    
    /***********************************************
    * Simple Tree Menu- (c) Dynamic Drive DHTML code library (www.dynamicdrive.com)
    * This notice MUST stay intact for legal use
    * Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
    ***********************************************/
    
    </script>
    <title>SmartStream: Videos</title>
    <link rel="stylesheet" type="text/css" href="simpletree.css" />
    </head>
    
    <body>
        <h4>Available Movies</h4>
        <a href="./index.html"><h4>Home Page</h4></a>
    <a href="javascript:ddtreemenu.flatten('treemenu1', 'expand')">Expand All</a> |
    <a href="javascript:ddtreemenu.flatten('treemenu1', 'contact')">Contract All</a>
    
    <ul id="treemenu1" class="treeview">
    
    ''')
    
    CreateNestedElements(TheFilms, IndexHtml)
    
    IndexHtml.write('''
                    
                    </ul>
                    <script type="text/javascript">
                    ddtreemenu.createTree("treemenu1", true)
                    </script>
                    </body>
                    </html>
                    ''')
    IndexHtml.close()
    
