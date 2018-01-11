
"""
Simple example to show how to use cherrypy with jquery and jquery mobile.
https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=29924
https://www.virag.si/2012/11/streaming-live-webm-video-with-ffmpeg/
http://www.creativebloq.com/html5/build-custom-html5-video-player-9134473
"""
import RPi.GPIO as GPIO
from time import sleep
from time import time
import os
import subprocess
import cherrypy
import pipan

GPIO.setmode(GPIO.BCM)

GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

Motor1 = GPIO.PWM(11, 10)
Motor1.start(0)
Motor2 = GPIO.PWM(7, 8)
Motor1.start(0)
speed = 50
speedt = 5

def forward(speed):
  GPIO.output(9,GPIO.LOW)
  GPIO.output(10,GPIO.HIGH)
  GPIO.output(7,GPIO.HIGH)
  GPIO.output(8,GPIO.LOW)
  Motor1.ChangeDutyCycle(speed)
  Motor2.ChangeDutyCycle(speed)

def backward(speed):
  GPIO.output(9,GPIO.HIGH)
  GPIO.output(10,GPIO.LOW)
  GPIO.output(7,GPIO.LOW)
  GPIO.output(8,GPIO.HIGH)
  Motor1.ChangeDutyCycle(speed)
  Motor2.ChangeDutyCycle(speed)

def stop():
  GPIO.output(9,GPIO.LOW)
  GPIO.output(10,GPIO.LOW)
  GPIO.output(11,GPIO.LOW)
  GPIO.output(7,GPIO.LOW)
  GPIO.output(8,GPIO.LOW)

def left(speedt):
  GPIO.output(9,GPIO.LOW)
  GPIO.output(10,GPIO.HIGH)
  GPIO.output(7,GPIO.LOW)
  GPIO.output(8,GPIO.HIGH)
  Motor1.ChangeDutyCycle(speedt)
  Motor2.ChangeDutyCycle(speedt)

def leftc():
  string = "echo 5=+10 > /dev/servoblaster"
  os.system(string)
  sleep(1)

def right():
  GPIO.output(9,GPIO.HIGH)
  GPIO.output(10,GPIO.LOW)
  GPIO.output(7,GPIO.HIGH)
  GPIO.output(8,GPIO.LOW)
  Motor1.ChangeDutyCycle(speedt)
  Motor2.ChangeDutyCycle(speedt)

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
  p.neutral_pan()
  p.neutral_panc()
  p.neutral_panu()
  p.neutral_tiltc()
  sleep(1)

def distance():
  sonar = subprocess.Popen(['./sonar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
  out = sonar.communicate()  
  return out

class HelloWorld:
    """ Sample request handler class. """
    @cherrypy.expose
    def index(self,distance=distance()):
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
              $("#fwd").mousedown(function () {$.post('/request',{key_pressed:"fwd"})});
              $("#fwd").mouseup(function () {$.post('/request',{key_pressed:"stop"})});
              $("#rev").mousedown(function () {$.post('/request',{key_pressed:"rev"})});
              $("#rev").mouseup(function () {$.post('/request',{key_pressed:"stop"})});
              $("#neutral").click(function () {$.post('/request',{key_pressed:"neutral"})});
              $("#left").click(function () {$.post('/request',{key_pressed:"left"})});
              $("#right").click(function () {$.post('/request',{key_pressed:"right"})});
              $("#power").change(function () {$.post('/request',{key_pressed:"power_"+$(this).val()})});

            document.addEventListener('keydown', function(event) {
              if (event.keyCode == 37) {$.post('/request',{key_pressed:"left"})}
              if (event.keyCode == 38) {$.post('/request',{key_pressed:"fwd"})}
              if (event.keyCode == 39) {$.post('/request',{key_pressed:"right"})}
              if (event.keyCode == 32) {$.post('/request',{key_pressed:"neutral"})}
              if (event.keyCode == 87) {$.post('/request',{key_pressed:"upc"})}
              if (event.keyCode == 83) {$.post('/request',{key_pressed:"downc"})}
              if (event.keyCode == 65) {$.post('/request',{key_pressed:"leftc"})}
              if (event.keyCode == 68) {$.post('/request',{key_pressed:"rightc"})}
              else if (event.keyCode == 40) {$.post('/request',{key_pressed:"rev"})}
            }, true); 

            document.addEventListener('keyup', function(event) {
              if (event.keyCode == 38) {$.post('/request',{key_pressed:"stop"})}
              else if (event.keyCode == 40) {$.post('/request',{key_pressed:"stop"})}
              else if (event.keyCode == 37) {$.post('/request',{key_pressed:"stop"})}
              else if (event.keyCode == 39) {$.post('/request',{key_pressed:"stop"})}
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
<center><iframe src="http://192.168.0.56:8080/stream/video.mjpeg" width="340" height="260"></iframe></center>
            <div data-role="content">
                <div class="ui-grid-c">
                    <div class="ui-block-a">
                        <button type="button" id="left" data-role="button" data-transition="fade" >
                            Left
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="fwd" data-role="button" data-transition="fade">
                            Forward
                        </button>
                    </div>
                    <div class="ui-block-b">
                        <button type="button" id="rev" data-role="button" data-transition="fade">
                            Reverse
                        </button>
                    </div>
                    <div class="ui-block-c">
                        <button type="button" id="right" data-role="button" data-transition="fade">
                            Right
                        </button>
                    </div>

                </div>
                <div data-role="fieldcontain">
                    <fieldset data-role="controlgroup">
                        <label for="power">
                        </label>
                        <select name="power smart" id="power" data-theme="a" data-role="slider">
                            <option value="off">
                                Off
                            </option>
                            <option value="on">
                                On
                            </option>
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
        if key == "fwd":
            forward(speed)
        elif key == "stop":
            stop()
        elif key == "rev":
            backward(speed)
        elif key == "left":
            left(speed)
        elif key == "right":
            right()
        elif key == "upc":
            upc()
        elif key == "downc":
            downc()
        elif key == "leftc":
            leftc()
        elif key == "rightc":
            rightc()
        elif key == "power_on":
            stop()
        elif key == "neutral":
            neutral()
            stop()
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
