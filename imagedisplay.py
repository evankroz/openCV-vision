import cv2 as cv

def displayimage(file_path):

    img = cv.imread(file_path)
    

    cv.imshow("image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    displayimage("burger.jpeg")