SmartStream
===========

Everything to setup a Streaming Server and WebInterface



Stub diagram: 

                                    +
     +-----------------+            |
     |                 |            |
     |                 |--> Ethernet|-> Web Interface -> Functions available:
     |  RaspberryPi    |            |                 +     * Stream a movie in the browser(Choose
     |                 |            |                 |       from index)
     |                 |            |                 |     * Output the movie through HDMI
     +-----------------+            |                 |
        +                           |                 |
        |                           |                 |
        +-->Source HardDisk         |                 |
                                    |                 |
                                    |                 |
                                    |                 +--> Button to force the creation of an index
+-----------------------------------+
