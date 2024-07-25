import numpy as np
import cv2
import cv2.aruco as aruco
import time

arucoDict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)
for num in range(1,25):
    print("Cube No '{}'".format(num))
    for side in range(1,7):
        if num < 10:
            id_str = "0" + str(num) + str(side)
        else:
            id_str = str(num) + str(side)
        id = int(id_str)
        tag = np.zeros((300, 300, 1), dtype="uint8")
        aruco.generateImageMarker(arucoDict, id, 300, tag, 1)
        cv2.imwrite("{}.png".format(id_str), tag)
        
print("Successfully created all the ArUCo Markers.")
