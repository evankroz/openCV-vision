import cv2

image = cv2.imread("images/road.jpeg")
image2 = cv2.imread("images/burger.jpeg")

h1, w1 = image.shape[:2]
h2, w2 = image2.shape[:2]

count = 0
while count < 1000:
    for i in range(1000):
        (B, G, R) = image[1+i,100] #apprentely cv2, extracts in blue, gree, red, not RGB?, weird.....
        print(f"R = {R}. G = {G}, B = {B}")
        count += 1
print(f"W1 = {w1}, H1 = {h1} \nW2 = {w2}, H2 {h2}")