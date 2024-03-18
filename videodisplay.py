import cv2 as cv

def play_video(file_path):

    cap = cv.VideoCapture(file_path)

    while cap.isopened():
        ret, frame = cap.read()
        frame = cv.resize(frame, fx = 0.5, fy = 0.5)

        while ret == True:
            cv.imshow(frame)

            if cv.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            break
cap.release()
cap.destroyAllWindows()

if __name__ == "__main__":
    play_video("highway.mp4")