# <u> Python OpenCV Method Cheat Sheet [cv2] </u>

##### <u><I> GUI Related Methods & Image/Video Loading</I></u>


* **cv2.imread(path, image_type = cv2.IMREAD_COLOR)**
  * This method scans in an image using a relative path on the current project directory, or an absolute path. The second arguments can take on the following values

    * cv2.IMREAD_COLOR [*default arg*] or 1. Loads image in color, but neglects transparency in the alpha channel. BGR format.

    * cv2.IMREAD_GRAYSCALE or 0. Loads image in grayscale.

    * cv2.IMREAD_UNCHANGED or -1. Loads the image in with the alpha channel.


* **cv2.imshow(window_name, image)**
  * Opens a new window. The title at the top of the window is assigned by window_name, and the image displayed inside of the actual window is the image.


* **cv2.namedWindows(widow_name, flag)**
  * this function creates a new window. *This is different than cv2.imshow() because the image does NOT need to be loaded when the window is constructed.* The flag arg can be set to the following options.
    * cv2.WINDOW_AUTOSIZE [*default arg*]. Automatically generates a set size.

    * cv2.WINDOW_NORMAL. Image can be resized, and gets a track bar if needed. May be useful to resize the image from webcam feeds from convenience.

* **cv2.waitKey(time)**
  * This function waits up to the number of milliseconds specified by the time parameter. If 0 is passed, it waits indefinitely.

* **cv2.destroyAllWindows()**
  * Destroys all active windows created by the user.

* **cv2.destroyWindow(window_name)**
  * Destroys only the window with the same name as the name given as a parameter.

* **cv2.imwrite(filename, img[parameters])**
  * Saves the image passed in as a parameter to a file in the current directory. *The file type is dictated by the extension on the string passed in as the file name.*

-----------------------------------------------------------------
[Video processing basics]

* **cv2.VideoCapture(camera_num)**
  * Constructor for VideoCapture objects. Passing 0 or -1 as the arg will select the first/default camera. Passing 1 will select the second camera as prioritized by the system, etc.
    * Constructor can also be initialized with a video file, in which case it will be read in as a file stream.

* **&lt;VideoCapture&gt;.read()**
  * Returns parameters *(retval, image)*, where *retval* is a boolean indicating whether or not the image capture was successful, and image is the actual image scan (Assign as a tuple),


* **&lt;VideoCapture&gt;.isOpened()**
  * Returns a boolean if the VideoCapture object has been initialized correctly.

* **&lt;VideoCapture&gt;.open()**
  * Initializes the VideoCapture object. Should be called if <VideoCapture>.isOpened() returns false.

* **&lt;VideoCapture&gt;.get(property_number)**
** &lt;VideoCapture&gt;.set(property_number, new_value)**
  * Changes basic properties of the incoming feed. For a full list of properties, see: [Image Properties.](http://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html#aa6480e6972ef4c00d74814ec841a2939&gsc.tab=0)

* **&lt;VideoCapture&gt;.release()**
  * Releases the resources allocated by the camera object upon call.

* **&lt;VideoWriter&gt;.release()**
  * Releases the resources allocated by the video writer object upon call.

* **cv2.VideoWriter(file_name,fourcc_code, fps, (frame_height, frame_width), isColor=False)**
  * This method is used for constructing a VideoWriter object that can be used to export videos. file_name represents the output of the method. All parameters are fairly self-explanatory except for fourcc_code, which has to do with the compression format (see [fourcc_info](http://www.fourcc.org/codecs.php) for a list of codes).
    * The object passed into fourcc_code should ** not ** be a string. You should call the following method (as shown) and pass the return value into the VideoWriter constructor.
    ```Python
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    ```

* **&lt;VideoWriter&gt;.write(frame)**
  * Assigns the write frame to the VideoWriter (usually called in a loop to build the video frame by frame).

--------------------------------------------------------------------
[Drawing on frames in CV]

** This is really easy, and not super relevant to BrickVision. Fill me in at a later date, but here are some pretty easy tutorials to follow on the subject:** [drawing_stuff.](http://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html#gsc.tab=0)

[Mouse_as_paintbrush.](http://docs.opencv.org/master/db/d5b/tutorial_py_mouse_handling.html#gsc.tab=0)

--------------------------------------------------------------------
