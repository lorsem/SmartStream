#!/usr/bin/env python

import pickle
import cgi
import cgitb
cgitb.enable()

def CreateNestedElements(TheFilms, IndexHtml):
    for Name  in TheFilms.keys():
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
                            '''.format('/cgi-bin/ShowVideo.py?VidPath={}&VidName={}"ciccia'.format('/' + TheFilms[Name], Name),
                                       Name)
                           )
    


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

<a href="javascript:ddtreemenu.flatten('treemenu1', 'expand')">Expand All</a> |
<a href="javascript:ddtreemenu.flatten('treemenu1', 'contact')">Contact All</a>

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
print "Content-Type: text/html; charset=UTF-8"
print ''
print '''
<html><body>DONE</body></html>
'''
