
import cv2
import numpy as np


MOG2_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

bg_subtractor=MOG2_subtractor

def objecttrack(file_path):
    cap = cv2.VideoCapture(file_path)

    while True:
        ret, frame = cap.read()

        foreground_mask = bg_subtractor.apply(frame)

        ret , treshold = cv2.threshold(foreground_mask.copy(), 120, 255,cv2.THRESH_BINARY)
        
        dilated = cv2.dilate(treshold,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)),iterations = 2)
        
        contours, hier = cv2.findContours(dilated,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            if cv2.contourArea(contour) > 50:
                (x,y,w,h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 0), 2)

        cv2.imshow("Subtractor", foreground_mask)
        cv2.imshow("threshold", treshold)
        cv2.imshow("detection", frame)
        
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break
            
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    objecttrack("highway.mp4")