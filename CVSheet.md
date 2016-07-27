# <u> Python OpenCV Method Cheat Sheet [cv2] </u><br>
&lt;Created by Alexander Brooks&gt;
##### <u><I> GUI Related Methods & Image/Video Loading</I></u><br>
* **cv2.imread(path, image_type = cv2.IMREAD_COLOR)**<br>
  * This method scans in an image using a relative path on the current project directory, or an absolute path. The second arguments can take on the following values

    * cv2.IMREAD_COLOR [*default arg*] or 1. Loads image in color, but neglects transparency in the alpha channel. BGR format.

    * cv2.IMREAD_GRAYSCALE or 0. Loads image in grayscale.

    * cv2.IMREAD_UNCHANGED or -1. Loads the image in with the alpha channel.
<br><br>
* **cv2.imshow(window_name, image)**

  * Opens a new window. The title at the top of the window is assigned by window_name, and the image displayed inside of the actual window is the image.
<br><br><br>
* **cv2.namedWindows(widow_name, flag)**<br>
  * this function creates a new window. *This is different than cv2.imshow() because the image does NOT need to be loaded when the window is constructed.* The flag arg can be set to the following options.
    * cv2.WINDOW_AUTOSIZE [*default arg*]. Automatically generates a set size.

    * cv2.WINDOW_NORMAL. Image can be resized, and gets a track bar if needed. May be useful to resize the image from webcam feeds from convenience.
<br><br>
* **cv2.waitKey(time)**<br><br>
  * This function waits up to the number of milliseconds specified by the time parameter. If 0 is passed, it waits indefinitely.
<br><br><br>
* **cv2.destroyAllWindows()**<br><br>
  * Destroys all active windows created by the user.
<br><br><br>
* **cv2.destroyWindow(window_name)**<br><br>
  * Destroys only the window with the same name as the name given as a parameter.
<br><br><br>
* **cv2.imwrite(filename, img[parameters])**<br><br>
  * Saves the image passed in as a parameter to a file in the current directory. *The file type is dictated by the extension on the string passed in as the file name.*
<br><br><br>
* **cv2.cvtColor(image, conversion)**<br><br>
  * Converts the image to a different type (used for masking). Available options are in the form as follows, and are pretty self-explanatory.
    * cv2.COLOR_BGR2GRAY
    * cv2.COLOR_BGR2HSV
<br><br><br>
* **cv2.moveWindow(winname, x, y)**<br><br>
  * Moves the window to the appropriate position (useful so that your windows do not open on top of each other every time. See code below for an example).
<br><br><br>
* **&lt;image&gt;.shape**<br><br>
  * calling this attribute returns the number of rows, columns, and channels of the image. It is *very* useful for image spacing and capturing a region of interest.
  <br><br><br>

<u>SECTION SAMPLE CODE</u>

```python
'''Demonstrates basic image operations. Use the current directory to see the image.'''
import cv2
import numpy as np
import matplotlib as mlp

if __name__ == '__main__': #Python's equivalent of main()
    my_image = cv2.imread('puppy.jpg', cv2.IMREAD_COLOR) #scan the image in from the current directory

    (rows, cols, channels) = my_image.shape #immediately store the dimensions of the image.

    cv2.imshow('Dog Picture!', my_image) #show the image
    cv2.imshow('Gray Dog!', cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)) #convert to grayscale and show that also!

    cv2.moveWindow('Dog Picture!', 0, 0) #move the images so they are not on top of each other
    cv2.moveWindow('Gray Dog!', 0, rows) #note how we can use the shape attribute to space our images out well.

    cv2.waitKey(0) #wait until the user does something.
    cv2.destroyAllWindows() #close the windows and exit.
    cv2.waitKey(1) #necessary on UNIX based systems. Just put it after close because reasons.

```

-----------------------------------------------------------------

##### <u><I> Video Processing Basics</I></u><br>
* **cv2.VideoCapture(camera_num)**<br>
  * Constructor for VideoCapture objects. Passing 0 or -1 as the arg will select the first/default camera. Passing 1 will select the second camera as prioritized by the system, etc.
    * Constructor can also be initialized with a video file, in which case it will be read in as a file stream.
<br><br>

* **&lt;VideoCapture&gt;.read()**
  * Returns parameters *(retval, image)*, where *retval* is a boolean indicating whether or not the image capture was successful, and image is the actual image scan (Assign as a tuple),
<br><br><br>

* **&lt;VideoCapture&gt;.isOpened()**<br>
  * Returns a boolean if the VideoCapture object has been initialized correctly.
<br><br>
* **&lt;VideoCapture&gt;.open()**<br><br>
  * Initializes the VideoCapture object. Should be called if <VideoCapture>.isOpened() returns false.
<br><br><br>
* **&lt;VideoCapture&gt;.get(property_number)**<br>
** &lt;VideoCapture&gt;.set(property_number, new_value)**
  * Changes basic properties of the incoming feed. For a full list of properties, see: [Image Properties.](http://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html#aa6480e6972ef4c00d74814ec841a2939&gsc.tab=0)<br><br><br>

* **&lt;VideoCapture&gt;.release()**<br>
  * Releases the resources allocated by the camera object upon call.
<br><br><br>
* **&lt;VideoWriter&gt;.release()**<br><br>
  * Releases the resources allocated by the video writer object upon call.
<br><br><br>
* **cv2.VideoWriter(file_name,fourcc_code, fps, (frame_height, frame_width), isColor=False)**<br><br>
  * This method is used for constructing a VideoWriter object that can be used to export videos. file_name represents the output of the method. All parameters are fairly self-explanatory except for fourcc_code, which has to do with the compression format (see [fourcc_info](http://www.fourcc.org/codecs.php) for a list of codes).
    * The object passed into fourcc_code should ** not ** be a string. You should call the following method (as shown) and pass the return value into the VideoWriter constructor.
    ```python
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    ```
<br><br><br>
* **&lt;VideoWriter&gt;.write(frame)**<br><br>
  * Assigns the write frame to the VideoWriter (usually called in a loop to build the video frame by frame).
<br><br><br>

<u>SECTION SAMPLE CODE</u>

```python
import cv2
import numpy as np
import matplotlib as mlp

if __name__ == '__main__':
  cap = cv2.VideoCapture(0) #open the camera
  flip = False #default to color

  if(not cap.isOpened()): #check to make sure things opened correctly
    cap = cap.Open()

  while True:
    (_, my_image) = cap.read() #ignore _, get image from camera.
    keyGrab = cv2.waitKey(35) #roughly 30 fps

    if keyGrab == ord('q'): #only care if user presses q (close windows) or g (switch between grayscale and color)
      break
    elif keyGrab == ord('g'):
        flip = not flip #invert toggle
        cv2.waitKey(250) #give the user time to release the key (will flash if held down)

    if flip == False:
        cv2.imshow('A head!', my_image)#show color feed
    if flip == True:
        cv2.imshow('A head!', cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY))#show grayscale feed

  cv2.destroyAllWindows()
  cv2.waitKey(1)
  cap.release() #release the camera resource
```

--------------------------------------------------------------------
##### <u>[Drawing on frames in CV]</u><br>
* **cv2.line(image, (x1, y1), (x2, y2), (b, g, r), width)**<br>
  * Draws a line on the image from pixel coordinates (x1, y1) to (x2, y2). The tuple (b, g, r) is the color of the line, and the width is specified in pixels.
  <br><br><br>

* **cv2.rectangle(image, (x1, y1), (x2, y2), (b, g, r), width)**
  * Draws a rectangle on the image. Pixel coordinates (x1, y1) represent the top left corner, and (x2, y2) represent the bottom right corner.
<br><br><br>
* **cv2.circle(image, (x, y), radius, (b, g, r), width)**<br><br>
  * Draws a circle on the image centered at (x, y).
<br><br><br>
* **cv2.polylines(image, [points], Status, (b, g, r), width)**<br><br>
  * Same as the other shapes, except [points] is a numpy array defining each of the points in the function. If the Status parameter is True, the polygon will be closed, otherwise it will be left open!
<br><br><br>
* **cv2.putText(image, image_text, (x, y), font_object, size, (b, g, r), spacing, Anti-aliasing)**<br><br>
  * Writes the text beginning at (x, y). font_objects are of the form cv2.<font> (see list online).


*NOTE: If width < 0 for any shapes, the shape will be filled in! Otherwise it is hollow.*
<br><br><br>

<u>SECTION SAMPLE CODE</u>


```python
import cv2
import numpy as np
import matplotlib as mlp

if __name__ == '__main__':
  size = (width, height, channels) = (200, 200, 3) # create the dimensions. 200 X 200 pixes, BGR (3 channels)
  blank_image = np.zeros(size, np.uint8) #(0,0,0) = black, so this is just a black square
  cv2.imshow('black', blank_image)
  cv2.moveWindow('black', 0, 0) #move to top left corner.
  cv2.waitKey(0)

  cv2.line(blank_image, (0,0), (200, 200), (125, 125, 0), 5) #draw a diagonal line through the numpy array
  cv2.imshow('line', blank_image) #display the update (drawn line)
  cv2.moveWindow('line', 200, 0)
  cv2.waitKey(0)

  cv2.rectangle(blank_image, (50, 50), (150, 150), (0, 125, 125), -1) #draw a solid yellow rectangle. NOTE: The line is OVERWRITTEN. The values are NOT added.
  cv2.imshow('rectLine', blank_image)
  cv2.moveWindow('rectLine', 400, 0)
  cv2.waitKey(0)

  cv2.circle(blank_image, (100,100), 50,(255, 0, 0), 2) # draw a hollow blue circle.
  cv2.imshow('circRectLine', blank_image)
  cv2.moveWindow('circRectLine', 600, 0)
  cv2.waitKey(0)

  pts = np.array([(50, 50), (100, 100), (50, 75)], np.int32) #points for a triangle as a numpy array
  pts = pts.reshape(-1, 1, 2) #group the points. -1 infers the 3rd dimension from (1, 2), but this should work for anything in opencv
  cv2.polylines(blank_image, [pts], True, (255, 255, 255), 1) #draw the triangle. make sure [pts] is passed as a list.
  cv2.imshow('allShapes', blank_image)
  cv2.moveWindow('allShapes', 800, 0)
  cv2.waitKey(0)

  cv2.putText(blank_image, 'PUPPIES ARE CUTE', (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2) #write "PUPPIES ARE CUTE" starting at (10, 200) in the preset font, and a gentle purple color.
  cv2.imshow('FRIENDS', blank_image)
  cv2.moveWindow('FRIENDS', 1000, 0)
  cv2.imwrite("art.jpg", blank_image) #save the image to the current directory
  #note: OPENCV WILL NOT TELL YOU IF YOU ARE WRITING OUTSIDE OF THE PIXEL DIMENSIONS. IT JUST WON'T SHOW UP AS ANYTHING ON YOUR SCREEN!
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  cv2.waitKey(1)

```


--------------------------------------------------------------------

##### <u>Image Operators</u> [INCOMPLETE]
*NOTE:Remember that (0,0,0) is a black image and (255, 255, 255) is a white image.*

* **basic image addition**
  * Two types [+ and the openCV add method]. We could call them as follows.

  ```python
  #say we have puppies.png and kitties.png in the local directory.

  img1 = imread('puppy.png') #colored image by default
  img2 = imread('kitty.png')

  imgSum = img1 + img2  
  cvSum = cv2.add(img1, img2)

  imshow('+ operator', imgSum) #display the result
  imshow('cv add', cvSum)

  cv2.waitKey(0) #wait for a key press
  cv2.destroyAllWindows()
  ```
    * If you actually do this, you'll probably find that the cv window has a lot of white. This is because the cv2.add() method is a **saturating** operation (meaning any values exceeding 255 are set to 255). In contrast, the numpy addition operation on the image is a **modulo** operation on the tuple!

**weighted image addition**
* **cv2.addWeighted(img1, weight1, img2, weight2, gamma)**
  * Similar functionality to the cv2.add() method, but more efficient as it weighs the images against each other instead of simply throwing them on top of each other at full force (AKA this is less likely to cap out at 255). The weight values are decimals, so weight1 + weight2 = 1. The gamma parameter is a scalar that is added to each sum.


**Accessing specific sections of the image**
To access a specific pixel region, we can just invoke the image as a two dimensional array (also note that Python supports Matlab style slicing). For instance, the following code would grab part of the puppies.png image that we could use for manipulation.
```python
  img1 = imread('puppies.png')
  subset = img1[50:100, 50:100] #note that nothing is displayed.
  cv2.waitKey(0)
```
*Note: The origin is generally the <u>top left</u> of the image.*

**Bitwise operators on images**

*IMPORTANT: Usually, image processing is done by reading an image in with full color, duplicating it in grayscale, analyzing the grayscale image, and then making the appropriate changes on the corresponding pixels of the color image.*
