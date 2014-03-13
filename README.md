SmartStream
===========

Everything to setup a Streaming Server and WebInterface



Stub diagram: 




<pre>                               
     +-----------------+            
     |                 |            
     |                 |--&gt; Ethernet -&gt; Web Interface -&gt; Functions available:
     |  RaspberryPi    |                             +     * Stream a movie in the browser(Choose
     |                 |                             |       from index)
     |                 |                             |     * Output the movie through HDMI
     +-----------------+                             |
        +                                            |
        |                                            |
        +--&gt;Source HardDisk                          |
                                                     |
                                                     |
                                                     +--&gt; Button to force the creation of an index
</pre>


### How it should work:
When plugged in, the HD is searched for videos. An index is created without moving the files. From the index, users can stream videos from their computers in the browser or ask the server to start the output of a video through HDMI.
The indexing will likely be implemented in a Python script, run on the server when needed. Files will be embedded in HTML5. Conversion won't be possible due to the RP's limited computing capabilities. HTML5 videos can be any format and will be played as long as the default player (e.g. QuickTime on Macs) supports the format. If the user chooses to play the film on HDMI, the RP should play the video through the HDMI port. 

### Fair and beautiful main page
On the main page will be possible to:
- Select a movie from index -> stream on webbrowser or through HDMI
- Upload or remove a movie 
- Manually organize datas on HD -> rename, move, copy, upload, remove (kinda DropBox-like)

The index is always going to be updated to list ALL the movies. If needed indexing can be set to operate on a specific directory, for example "Films", in case you have other videos you don't want to be indexed on the main page (e.g. porns)
