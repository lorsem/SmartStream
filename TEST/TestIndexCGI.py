import pickle


def Create_nested_elements(TheFilms, IndexHtml):
    for Name  in TheFilms.keys():
        if type(TheFilms[Name]) == dict:
            IndexHtml.write('''
                            <br>
                            <li>{}
                            <ul>
                            '''.format(Name))
            Create_nested_elements(TheFilms[Name], IndexHtml)
            IndexHtml.write('''
                            </ul>
                            </li>
                            ''')
        else:
            IndexHtml.write('''<br><li><a href = "{0}">{1}</a></li>
                            '''.format('./ShowVideo.py?VidPath='.format('/' + TheFilms[Name]), Name))
        
            



dump = open('DUmpFile.pkl', 'rb')
dizio = pickle.load(dump)
index = open ('indexTEST.html', 'w')
index.write(
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

<link rel="stylesheet" type="text/css" href="simpletree.css" />
</head>

<body>
    <h4>Available Movies</h4>

<a href="javascript:ddtreemenu.flatten('treemenu1', 'expand')">Expand All</a> | <a href="javascript:ddtreemenu.flatten('treemenu1', 'contact')">Contact All</a>

<ul id="treemenu1" class="treeview">

''')

Create_nested_elements(dizio, index)
index.write('''
                </ul>
                <script type="text/javascript">
                ddtreemenu.createTree("treemenu1", true)
                </script>
                </body>
                </html>
                ''')
index.close()




