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


###How it should work:
When plugged in, the HD is searched for videos. An index is created without moving the files. From the index, users can stream videos from their computers in the browser or ask the server to start the output of a video through HDMI.
The indexing will likely be implemented in a Python script, run on the server when needed. Files will be embedded in HTML5. Conversion won't be possible due to the RP's limited computing capabilities. HTML5 videos can be any format and will be played as long as the default player (e.g. QuickTime on Macs) supports the format. If the user chooses to play the film on HDMI, the RP should play the video through the HDMI port. 
