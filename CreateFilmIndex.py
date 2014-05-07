#!/usr/bin/env python

# The core of this script is IndexEverything. It is passed a dictionary or opens
#   a pickle-ed file if no dictiornary is passed(WARING: deprecated!). Then it
#   creates a nested menu    with directories/films. Links to film are calls to
#   ShowVideo (will add   option to set default to ShowVideo OR ShowVideo_vlc)

import pickle
import cgi
import cgitb
cgi.StringIO()

cgitb.enable()


def CreateNestedElements(TheFilms, IndexHtml):
    for Name in sorted(TheFilms.iterkeys()):
        # If it is a directory on the filesystem, it is a dictionary in our
        #   abstraction
        if type(TheFilms[Name]) == dict:
            # Head of html for js Finder-like folders ('|> Folder' in Html output)
            IndexHtml.write('''
                            <div class="demo-frame">
                                <div id="toggleState">
                                    <a class="expander"  href="#">{}</a>
                                        <div class="content">
                            '''.format(Name)
                           )
            # Recursively calls itself for every nested directory
            CreateNestedElements(TheFilms[Name], IndexHtml)
            IndexHtml.write('''
                                        </div>
                                </div>
                            </div>
                            ''')
        else:   # If it is a file, treat it correctly.
            IndexHtml.write('''
                            <a href="{0}"><div class="videoImage">{1}</div></a>
                            '''.format('/cgi-bin/ShowVideo.py?VidPath={}&VidName={}'.format('/' +
                                                             TheFilms[Name],
                                                             Name),
                                                            Name
                                       )
                           )

def IndexEverything(Index = None):
    if Index == None:    # Now deprecated, useful (maybe) for debugging
        Index = open ('index.pkl', 'rb')
        TheFilms = pickle.load(Index)
    else:    # If an index is passed to the function, it must be used!
        TheFilms = Index
    IndexHtml = open('/var/www/index.html', 'w')
    #head part of page:
    IndexHtml.write(

        '''\

<html>
<head>
    <link rel="stylesheet" type="text/css" href="/PageStyle.css" />
    <link rel="SHORTCUT ICON" HREF="/wallpapers/icon_small.png">
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <script type="text/javascript" src="/ExpandCollapse.js"></script>
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
        <a href="/">
            <img src="/wallpapers/Logo.png" alt="SmartStream" /></a>
                <div id="logo">
                </div>
        </div>
        <div id="body">
            <div id="list">
        ''')

    #Add all the nested content:
    # Here happens everything!
    CreateNestedElements(TheFilms, IndexHtml)

    #End the html tags as needed
    IndexHtml.write('''
            </div>
            <div id="menu">
                <div id="list">
                    <div class="demo-frame">
                        <div id="toggleState">
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

                <div class="demo-frame">
                        <div id="toggleState">
                            <a class="expander"  href="#">Upload Files</a>
                                <div class="content">
                                      <form enctype="multipart/form-data" action="/cgi-bin/fileUploader.py" method="post">
                                        File: <input type="file" name="file"><br>
                                        Hard Drive path (<i>Nothing</i> for root):
                                        <input name="dirName" type="text"  />
                                        <p><input type="submit" value="Upload"></p>
                                    </form>
                                </div>
                        </div>
                        </div>
                    </div>
            </div>
        </div>
    </div>
    </body>

</html>
''')
    #Close the index file
    IndexHtml.close()
