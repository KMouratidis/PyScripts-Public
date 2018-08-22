<h2> Edge detection</h2>
A script that uses OpenCV to perform simple edge detection. 
The original purpose was to detect outlines of objects on a table using the RaspberryPi.
Added some extra windows to show intermediate changes.

<h3>Usage:</h3>

```
>> python edge_detection.py -i "image-path.jpg"
>> python edge_detection.py --image "image-path.jpg"
```

```
>> python edge_detection.py -v 0 # first camera
>> python edge_detection.py --video "path-to-video.mp4"
>> python edge_detection.py --video "http://192.168.1.2:8080/?action=stream" # stream

```

Example using image:
<img src="https://github.com/KMouratidis/PyScripts/blob/master/OpenCV/Edge%20Detection/edge_detection.png">

Example using video:
<img src="https://github.com/KMouratidis/PyScripts/blob/master/OpenCV/Edge%20Detection/video.png">
