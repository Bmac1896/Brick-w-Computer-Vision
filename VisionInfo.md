# <u> Important Algorithms for Hand Detection </u>
* [To be extended at a later date]
&lt;Alex Brooks and Brandon McDonald, 8/13/2016&gt;

*  ** To make me pretty in Atom.io, go to Packages->Markdown Preview->Toggle Preview.**

## <u> Sobel Operator Algorithm </u>

Sobel edge detection generally works in the following manner.

Imagine you are trying to detect the edges of an RGB image. the sobel operator relies primarily on detecting abrupt changes in color; any change larger than a predefined threshold value is marked as an edge. Taking this into consideration, we typically do the following.

* **Convert the image to grayscale.** This allows for an easier threshold structure, because it allows the user to only consider the severity of the change in the gray channel. In other words, you only have to worry about thresholding on the gray values instead of a combined threshold with the red, green, blue (and alpha if applicable) channels.


* **  Use the threshold to detect large changes using two images (horizontal and vertical).** Imagine that you have a grayscale image, and a straight edge. To create the horizontal image, you would place the ruler vertically at the left side, and slowly move it (pixel by pixel) to the right. Any abrupt changes would be marked as white pixels in the resulting binary image, and everything else would be black. *If you do this yourself, you will see that  moving from left to right with a threshold is good for detecting vertical walls.* Similarly, moving the straight edge from top to bottom would allow you to detect horizontal edges, thus you will end up with one binary (black + white) image containing the vertical edges, and another containing the horizontal edges.

* ** Superimpose the two binary images holding the vertical/horizontal edges respectively.** This is the resulting image displayed by using the Sobel operator on an image.

# <u> Canny Edge Detection Algorithm</u>

In principle, Canny Edge Detection is an *extension* of the Sobel Operator. The process is summarized below.

* **Consider the binary image that comes *out* of the Sobel Operator. This and the grayscale image are both considered in the Canny Edge Detection Process, which is described below.**

* **Slightly blur the original image.** Blurring the image a little bit makes the image less irregular, and also helps counterbalance arbitrary noise. By doing this, we help ensure that the image will be smoother/that the edges will be more uniform.

* ** Edges in the binary image are made a uniform width.** This is a little bit more involved mathematically, but all that you really need to know is that the edges are essentially converted to thinner (sometimes even one pixel) lines so that they are easier to discern.

* ** Hysteresis Thresholding.** This is the most important part of the Canny algorithm, because this is how we eliminate the noise. Again, the internals aren't super important because all of this is wrapped inside of Python, but basically what happens is that we set two threshold values (one low, and one high). We then iterate through the binary image. When we encounter a white pixel (edge), we first check to see if it is immediately touching another edge pixel. *If is touching another edge pixel, then the magnitude of the change in the grayscale value only needs to be greater than the lower threshold for the pixel to be an edge after Canny detection, but if it is not touching another edge pixel, the change in magnitude must be greater than the larger threshold specified.* This helps remove arbitrary pixels that are marked as edges, because they need to pass the higher threshold, while the actual edges that are prominent only need to pass through the low threshold.

----------------------------------------------------------------

### <u>Python Code & Algorithms &lt;Brick Vision&gt;</u>
* [To be extended at a later date]

### <u> Python Game Logic & Code </u>
* [To be extended at a later date]

```python
#paste any code here, and it will keep your formatting, as well as syntax highlighting! For example (delete when you put actual code here).

if __name__ == main:
    main()
else:
    return -1;
```
