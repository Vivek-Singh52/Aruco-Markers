import imutils
import cv2
import sys

image = cv2.imread("011.png")
image = imutils.resize(image, width=600)

arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)
arucoParams = cv2.aruco.DetectorParameters()
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

if len(corners) > 0:
    ids = ids.flatten()
    for (markerCorner, markerID) in zip(corners, ids):
        corners = markerCorner.reshape((4, 2))
        (topLeft, topRight, bottomRight, bottomLeft) = corners
        topRight = (int(topRight[0]), int(topRight[1]))
        bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
        bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
        topLeft = (int(topLeft[0]), int(topLeft[1]))
        
        # draw the bounding box of the ArUCo detection
        cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
        cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
        cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
        cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
        
        # compute and draw the center (x, y)-coordinates of the ArUco marker
        cX = int((topLeft[0] + bottomRight[0]) / 2.0)
        cY = int((topLeft[1] + bottomRight[1]) / 2.0)
        cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
        
        # draw the ArUco marker ID on the image
        cv2.putText(image, str(markerID),
                    (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        
        print("[INFO] ArUco marker ID: {}".format(markerID))
        print(markerID)
        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

