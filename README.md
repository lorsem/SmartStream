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

### Main page features
On the main page it is possible to:
- Select one video to watch from Finder-like file system browsing
- Trigger the indexing/re-indexing of videos
- Upload or remove a movie (works but problems with big files! )

The index is always going to be updated to list ALL the movies. If needed indexing can be set to operate on a specific directory, for example "Films", in case you have other videos you don't want to be indexed on the main page (e.g. porn)

### Specifications
Supported video extensions: ('.wmv', '.mov', '.mpg', '.avi', '.mp4', '.mkv', 'm4v','.flv') [in indexer.py]

### TODO
* HDMI-output: maybe use something like os.system('/bin/vlc "MyVideo.mkv" ')
* Manually organize data on HD -> rename, move, copy, upload, remove (kind of like DropBox)

### Easy setup
The server itself is default **Apache 2**. You need the videos to be in */var/www/video* or in subdirs of this directory.
I'm using a RaspberryPi and stored all the media in one external drive, mounted in /media/HDD. I set /var/www/video
to be a soft link to */media/HDD* and set Apache to follow symlinks. I left everything default, only changes I made
are permissions. It should be easy-peasy to recreate the same server at home.

### Complete guide for Raspberry pi
First of all install apache2:

```shell
sudo apt-get install apache2 -y
```

Now copy all the stuff in `/var/www` (ovverride index.html)

Place the python scripts in `/var/www/cgi-bin` and make them executable

```shell
mkdir cgi-bin
mv *py cgi-bin
cd cgi-bin
chmod +x *py
```

Create the directory "video" scanned by the indexer

```shell
mkdir /var/www/video
```

Set apache2 to use the pythons scripts in cgi-bin

(.... to be continued)
