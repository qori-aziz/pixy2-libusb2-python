import cv2
import pixy2_raw_frame as p

res = p.initializing()
if res != 0:
        print(res)
        quit()
while True:
        image = cv2.imread("out0.ppm")
        p.getFrame()
        cv2.imshow("Image", image)
        cv2.waitKey(1)
        # time.sleep(0.2)