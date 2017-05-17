# PiBot
Webserver written in Python with Cherrypy3 to drive raspberry pi pan tilt camera
## Installation
- clone this repo and also install:
- WiringPi
- sudo apt-get install -y python-cherrypy3 git uv4l uv4l-raspicam uv4l-raspicam-extras uv4l-server
- Change pins on pantilt.
- start uv4l-raspicam
- Change camera url.
- Change tutorial.conf file to suit youre needs

## Usage
- start servod
- python remote_control.py
- Browse to <raspberrypi:8090>
- Use wasd to move the camera

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
TODO: Write history

## Credits
TODO: Write credits

## License
TODO: Write license
