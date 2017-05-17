
"""
Simple example to show how to use cherrypy with jquery and jquery mobile.
https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=29924
https://www.virag.si/2012/11/streaming-live-webm-video-with-ffmpeg/
http://www.creativebloq.com/html5/build-custom-html5-video-player-9134473
"""
from time import sleep
from time import time
import os
import subprocess
import cherrypy
import pipan

def leftc():
  string = "echo 5=+10 > /dev/servoblaster"
  os.system(string)
  sleep(1)

def rightc():
  string = "echo 5=-10 > /dev/servoblaster"
  os.system(string)
  sleep(1)

def upc():
  string = "echo 2=-10 > /dev/servoblaster"
  os.system(string)
  sleep(1)

def downc():
  string = "echo 2=+10 > /dev/servoblaster"
  os.system(string)
  sleep(1)

def neutral():
  p = pipan.PiPan()
  p.neutral_panc()
  p.neutral_tiltc()
  sleep(1)

def servod(status):
  if status == "on":
    string = "servod"
  elif status == "off":
    string = "pkill servod"
  os.system(string)
  sleep(1)

def uv4l(status):
  if status == "on":
    string = "/etc/init.d/uv4l_raspicam start"
  elif status == "off":
    string = "/etc/init.d/uv4l_raspicam stop"
  os.system(string)
  sleep(1)

class HelloWorld:
    """ Sample request handler class. """
    @cherrypy.expose
    def index(self):
      return '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0;" />
        <meta name="viewport" content="width=device-width"/>
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <title>
        </title>
        <link rel="stylesheet" href="static/jquery.mobile-1.0.1.min.css" />
        <style>
            /* App custom styles */
        </style>
        <script src="static/jquery.min.js">
        </script>
        <script src="static/jquery.mobile-1.0.1.min.js">
        </script>
        <script type="text/javascript">
        $(document).ready(function() {

            //stop the page from doing a stretch from the top when dragged ;
            document.ontouchmove = function(event){ event.preventDefault(); };
            //move beyond the address  bar to hide ;
            window.scrollTo(0, 1);
            //start button click code;
              $("#upc").mousedown(function () {$.post('/request',{key_pressed:"upc"})});
              $("#downc").mousedown(function () {$.post('/request',{key_pressed:"downc"})});
              $("#neutral").click(function () {$.post('/request',{key_pressed:"neutral"})});
              $("#leftc").click(function () {$.post('/request',{key_pressed:"leftc"})});
              $("#rightc").click(function () {$.post('/request',{key_pressed:"rightc"})});
              $("#stream").change(function () {$.post('/request',{key_pressed:"stream_"+$(this).val()})});
              $("#servod").change(function () {$.post('/request',{key_pressed:"servod_"+$(this).val()})});

            document.addEventListener('keypress', function(event) {
              if (event.keyCode == 32) {$.post('/request',{key_pressed:"neutral"})}
              if (event.keyCode == 87) {$.post('/request',{key_pressed:"upc"})}
              if (event.keyCode == 83) {$.post('/request',{key_pressed:"downc"})}
              if (event.keyCode == 65) {$.post('/request',{key_pressed:"leftc"})}
              if (event.keyCode == 68) {$.post('/request',{key_pressed:"rightc"})}
            }, true); 
        });
        </script>
    </head>
    <body style="overflow: hidden;overflow-x:hidden;">
        <div data-role="page" data-theme="a" id="page1">
            <div data-theme="a" data-role="header" data-position="">
                <h5>
                    Web Remote Robot <br>
                </h5>
            </div>
<center><iframe src="http://camera4.agropi.net/stream/video.mjpeg" width="800" height="600"></iframe></center>
            <div data-role="content">
                <div class="ui-grid-c">
                    <div class="ui-block-a">
                        <button type="button" id="leftc" data-role="button" data-transition="fade" >
                            Left
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="upc" data-role="button" data-transition="fade">
                            Up
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="downc" data-role="button" data-transition="fade">
                            Down
                        </button>
                    </div>
                    <div class="ui-block-c">
                        <button type="button" id="rightc" data-role="button" data-transition="fade">
                            Right
                        </button>
                    </div>

                </div>
                <div data-role="fieldcontain">
                    <fieldset data-role="controlgroup">
                        <label for="stream"></label>
                        <select name="stream" id="stream" data-theme="a" data-role="slider">
                            <option value="off">Off</option>
                            <option value="on">On</option>
                        </select>
                        <label for="servod"></label>
                        <select name="servod" id="servod" data-theme="a" data-role="slider">
                            <option value="off">Off</option>
                            <option value="on">On</option>
                        </select>
                        <button type="button" id="neutral" data-role="button" data-transition="fade"> Neutral </button>
                    </fieldset>
                </div>
            </div>
        </div>
    </body>
</html>
'''
    @cherrypy.expose
    def request(self, **data):
        # Then to access the data do the following
        #print data
        key = data['key_pressed'].lower()
        if key == "upc":
            upc()
        elif key == "downc":
            downc()
        elif key == "leftc":
            leftc()
        elif key == "rightc":
            rightc()
        elif key == "stream_on":
            uv4l("on")
        elif key == "stream_off":
            uv4l("off")
        elif key == "servod_on":
            servod("on")
        elif key == "servod_off":
            servod("off")
        elif key == "neutral":
            neutral()

def index(self):
    host = cherrypy.request.headers('Host')
    return "You have successfully reached " + host
            
import os.path
tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(HelloWorld(), config=tutconf)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(HelloWorld(), config=tutconf)
