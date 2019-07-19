import cv2
import time
import numpy as np
import imutils
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image-path", help="Provide the image's path.")
ap.add_argument("-v", "--video", help="""Provide the video path or stream,
                or camera ID. Any valid input to cv2.VideoCapture""")

def main(image=None, camera=None):

    # This is used for masking brownish colors out
    min_YCrCb = np.array([0,70,70], np.uint8)
    max_YCrCb = np.array([255,170,125], np.uint8)

    if image is not None:
        img = cv2.imread(image)
        # resize for convenience
        img = imutils.resize(img, width=450)

    while True:

        if camera is not None:
            ret, img = camera.read()

        imageYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        # Find region with brownish colors
        brownRegion = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)
        # Convert image to only with brownish colors
        masked_img = cv2.bitwise_and(img, img, mask=brownRegion)

        edges = cv2.Canny(masked_img, 200, 200)

        cv2.imshow("frame", img)
        cv2.imshow("imageYCrCb", imageYCrCb)
        cv2.imshow("masked_img", masked_img)
        cv2.imshow("brownRegion", brownRegion)
        cv2.imshow("edges", edges)

        # hit Q to exit
        key = cv2.waitKey(25) & 0xFF
        if key == ord("q"):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":

    args = vars(ap.parse_args())
    video = args.get("video", 0)
    image = args.get("image_path", 0)

    if video:
        try:
            try:
                video = int(video)
                camera = cv2.VideoCapture(video)
            except ValueError:
                camera = cv2.VideoCapture(video)
            time.sleep(0.25)
            main(camera=camera)
        except Exception as e:
            print(e)
    elif image:
        if not os.path.exists(image):
            raise FileNotFoundError("File doesn't exist.")
        main(image=image)
    else:
        raise Exception("Error: No image or video given.")
