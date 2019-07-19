"""
Inspired by this solution written in C++
http://answers.opencv.org/question/73165/compute-dense-sift-features-in-opencv-30/
"""

import cv2
import matplotlib.pyplot as plt

def compute_dense_sift(img, step=40, extra_radius=10):
    """
    Takes an image shape and a step and returns
    keypoints, descriptors, and the dense_sift detector
    """

    kps = []
    for i in range(step, img.shape[0], step):
        for j in range(step, img.shape[1], step):
            kps.append(cv2.KeyPoint(j, i, step + extra_radius))

    dense_sift = cv2.xfeatures2d.SIFT_create()

    kps, desc = dense_sift.compute(img, kps)

    return kps, desc, dense_sift

def draw_keypoints(img, kps, color=(0,0,255),
                   flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS):
    """Takes an image and keypoints and plots them with matplotlib."""
    cp = img.copy()

    cv2.drawKeypoints(cp, kps, cp, color, flags=flags)

    plt.figure(figsize=(7,4))
    plt.imshow(cp)
    plt.show()


if __name__ == "__main__":

    img = cv2.imread("building.jpg")

    kps, desc, dsift = compute_dense_sift(img)
    draw_keypoints(img, kps)
