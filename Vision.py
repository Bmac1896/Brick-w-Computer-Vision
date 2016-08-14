
import cv2
import numpy as np
import matplotlib as plt
import sys

import argparse #flags and stuff

class Vision:

##############################################################################

    
    def setArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--debug', action = 'store_true', help='Enables debug trace.') #helpful if we lose the user
        parser.add_argument('-t', '--trace', action = 'store_true', help='Turns contours red when locked on to user.') #useful for seeing how frequently contours are being lost.
        parser.add_argument('-G', '--GUI', action = 'store_true', help='Gives user a track bar to override threshold parameters.') #useful for picking a good threshold.
        args = parser.parse_args() #read in arguments
        if args.debug:
            print('debugging trace is on.')
            self.debug = True
        if args.trace:
            print('Trace will emphasize locked contours.')
            self.trace = True
        if args.GUI:
            print('GUI enabled.')
            self.GUI = True


    
    def __init__(self, cap=cv2.VideoCapture(0)):      

        self.cap = cap #camera, defaults to the first one available (add command line support for override later.)
        
        # Original, grayscale, and thresholded image masks. 
        self.img = None
        self.gray = None
        self.thresh = None

        # current hand coordinates, capture status
        (self.xHand, self.yHand) = (None, None)
        self.handLocked = False

        #frames since last detection, last profile, and color of user's hand (taken from initial contour and updated with each capture)
        self.frameSkips = 0
        (self.lastX, self.lastY) = (None, None)
        self.handColor = None #grayscale level

        #command line options
        self.debug = False
        self.trace = False
        self.GUI = False


##############################################################################

        

    def filterImage(self):
        cv2.namedWindow('GUI')

        
        _, self.img = self.cap.read() # Grab image from the camera
        self.img = cv2.flip(self.img, flipCode = 1) #mirror the image        
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY) #convert color image to gray
        self.thresh = cv2.GaussianBlur(self.gray, self.getKernel(), 0) #blur the gray image with a large kernel. A LARGE KERNEL HELPS DESTROY THE TINY CONTOURS [see GUI for debug!] WHY??!?!?!
        _ , self.thresh = cv2.threshold(self.thresh, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) #threshold the blurred image.
        self.thresh = cv2.erode(self.thresh, None, iterations = 2)
        self.thresh = cv2.dilate(self.thresh, None, iterations = 2)

        
        self.thresh = cv2.adaptiveThreshold(self.thresh, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2) #check args here too.


        if self.GUI == True: # replace me
            debug_trace = cv2.cvtColor(self.thresh, cv2.COLOR_GRAY2BGR)
            self.processContours(debug_trace)
            debug_trace[self.yHand,:] = (0,0,255)
            debug_trace[:,self.xHand] = (0,0,255)
            cv2.imshow('GUI', debug_trace)

            
        if self.debug == True: 
            print 'Current threshold: (', self.getLow(), '/', self.getHigh(), ')'

        if self.trace == True: #GUI option also includes the trace. 
            debug_trace = cv2.cvtColor(self.thresh, cv2.COLOR_GRAY2BGR)
            self.processContours(debug_trace)
            debug_trace[self.yHand,:] = (0,0,255)
            debug_trace[:,self.xHand] = (0,0,255)

            
            
            cv2.imshow('threshold trace', debug_trace)


    def getKernel(self):
        if self.GUI == True:
            cv2.createTrackbar('Gaussian Kernel', 'GUI', 0, 60, lambda x:x)
            kSize = cv2.getTrackbarPos('Gaussian Kernel', 'GUI')
            if kSize % 2 == 0:
                kSize = kSize + 1
            if kSize < 0:
                kSize = 1
            return (kSize, kSize) 
        else:
            return (25, 25) #default kernel.

    

    def getLow(self): #determing the threshold values for the filter [low].
        if self.handColor is None:
            return 70
        else:
            return ((self.handColor - 25) if ((self.handColor - 25) >= 0) else 0)
            

    def getHigh(self): #determine the threshold values for the filter [high].
        if self.handColor is None:
            return 255
        else:
            return ((self.handColor + 25) if ((self.handColor + 25) <= 255) else 255)


    def processCycle(self):
        while True:
            self.filterImage()
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        self.cap = self.cap.release()
        cv2.destroyAllWindows()



    def extractCenter(self, interest):
        moment = cv2.moments(interest)
        cX = int(moment["m10"] / moment["m00"])
        cY = int(moment["m01"] / moment["m00"])
        print cX, cY, '\n'
        print self.xPercent(), '\n'
        return (cX, cY)
        

    def processContours(self, trace): #Draws the largest contour onto the trace.
        _, contours, hierarchy = cv2.findContours(self.thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        max_val = 0
        index = 0
        
        for i in range(len(contours)): #create vector to iterate over.
            current = contours[i]
            area = cv2.contourArea(current)

            if area > max_val:
                max_val = area
                index = i               
            
        cv2.drawContours(trace,contours,index,(0,255,0),3)
        if index <= (len(contours) - 1): #to ensure out of range issues don't magically occur
            (self.xHand, self.yHand) = self.extractCenter(contours[index]) #update!
        else:
            print 'magic is happening.', index, len(contours)


    def xPercent(self):
        height, width = self.gray.shape
        if self.xHand != None:
            return float(self.xHand)/width
        else:
            return float(width)/2


##############################################################################

    # apply additional stuff if everything is all caught! [last location]

    
##############################################################################
    #control flow for the filter.


##############################################################################




    

def main():
    current_img = Vision()
    current_img.setArgs() #enable debugging or tracing properties.
    current_img.processCycle() #loop unil breaking.

        

if __name__ == '__main__':
    main()
