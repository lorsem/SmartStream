#!/usr/bin/env python
# import cgi
import cgitb
cgitb.enable()
import pickle


def load_index(file_name="index.pkl"):
    with open(file_name, "rb") as index_file:
        index = pickle.load(index_file)
    return index

index = load_index()

print "Content-Type: text/html\n"

print '''\
<html>
<head>
<style type="text/css">
        html, body {
            /* height: auto; */
            /* width : auto; */
            /* background-color: red; */
        }
        #wrap {
            width : auto;
            height : 100%;
            margin: 0 auto;
            max-width: 1280px;
            /* max-height : 820px; */
            /* padding : 3%; */
            /* background-color: grey; */
        }
        #header {
            width : auto;
            height : 20%;
            /* padding:auto; */
            display: table-cell;
            vertical-align:center;
        }
        #body {
            width : auto;
            height : 75%;
        }
        #list {
            width : 75%;
            height:inherit;
            /* height : 100%; */
            overflow-y: scroll;
            overflow-x: hidden;
            background-color:black;
            float: left;
        }
        #title {
            font-family : helvetica;
            font-size: 40px;
            padding : auto ;
        }
        #body p {
            color : white;
            font : helvetica;
        }
        #menu {
            width: 20%;
            height:inherit;
            /* height: 100%; */
            float: right;
            background-color:black;
            overflow-y: scroll;
            overflow-x: hidden;
        }
        #footer{
            height:auto;
        }
    </style>
}
    </script>
</head>
<body>
<div id="wrap">
    <div id="header">
        <h3 id="title">SMARTSTREAM</h3>
        <div id="logo">
        </div>
    </div>
        <div id="body">
            <div id="list">
'''

for key, val in index.iteritems:
    print '''\
<a href="{}"><p>{}</p></a>\
'''.format(val, key)

print '''\
            </div>
            <div id="menu">
'''

for key, val in index.iteritems:
    print '''\
<a href="{}"><p>{}</p></a>\
'''.format(val, key)

print '''\
            </div>
        </div>
    <div id="footer">
        test
    </div>
</div>
</body>
</html>\
'''
