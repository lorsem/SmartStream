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
    for Name in TheFilms.iterkeys():
        if type(TheFilms[Name]) == dict:
            IndexHtml.write('''
                            <div class="demo-frame">
                                <div id="demo-with-image">
                                    <a class="expander"  href="#">{}</a>
                                        <div class="content">
                            '''.format(Name))
            CreateNestedElements(TheFilms[Name], IndexHtml)
            IndexHtml.write('''
                                        </div>
                                    </div>
                                </div>
                            ''')
        else:
            IndexHtml.write('''
                            <a href="{0}"><div class="videoImage">{1}</div></a>
                            '''.format('/cgi-bin/ShowVideo.py?VidPath={}&VidName={}'.format('/' + TheFilms[Name], Name),
                                       Name)
                           )
    
def IndexEverything(Index = None):
    if Index == None: 
        Index = open ('index.pkl', 'rb')
        TheFilms = pickle.load(Index)
    else:
        TheFilms = Index
    IndexHtml = open ('/var/www/index.html', 'w')
    #head part of page:
    IndexHtml.write(
        '''
    

<html>
<head>
    <link rel="stylesheet" type="text/css" href="PageStyle.css" />
    <link rel="SHORTCUT ICON" HREF="wallpapers/icon_small.png">
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <script type="text/javascript" src="ExpandCollapse.js"></script>
    <script type="text/javascript">
        $(function () {
            $('.expander').simpleexpand();
        });
    </script>
    <title>SmartStream Home Page</title>
</head>
<body>
    <div id="wrap"> 
        <div id="header">
            <img src="wallpapers/Logo.png" alt="SmartStream" />
                <div id="logo">
    
                </div>
        </div>
        <div id="body">
            <div id="list">
                
                
                        
                        
        ''')
    #Add all the nested content:
    CreateNestedElements(TheFilms, IndexHtml)
    #End the html tags as needed
    IndexHtml.write('''
                   
            </div>
            <div id="menu">
                <div id="list">
                    <div class="demo-frame">
                        <div id="demo-with-image">
                            <a class="expander"  href="#">Create/Recreate Index</a>
                                <div class="content">
                                    <form name="Index_form" action="./cgi-bin/Server.py" method="POST">
                                        Path to Index (<i>Nothing</i> for default):
                                        <br  />
                                        <input name="scanDir" type="text"  />
                                        <br  />
                                        <input type="submit" value="submit">
                                    </form> 
                                </div>
                        </div>
                    </div>
                </div>
            </div>
            <div id="footer">
                <b>Footer</b>
            </div>
        </div>
    </div>
    </body>

</html>
''')
    #Close the index file 
    IndexHtml.close()
    
