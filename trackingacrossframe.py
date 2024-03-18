import cv2
#from google.colab.patches import cv2_imshow
import numpy as np


cap = cv2.VideoCapture("video.mp4")
ret, frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
keypoints, descriptors = orb.detectAndCompute(gray, None)

while cap.isOpened():
    ret, next_frame = cap.read()

    if not ret:
        break

    next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)

    next_keypoints, next_descriptors = orb.detectAndCompute(next_gray, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors, next_descriptors)

    matches = sorted(matches, key=lambda x: x.distance)

    matched_frame = cv2.drawMatches(frame, keypoints, next_frame, next_keypoints, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2_imshow(matched_frame)

    frame = next_frame
    keypoints = next_keypoints
    descriptors = next_descriptors

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()