import cv2
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import skimage.measure
import matplotlib.pyplot as plt

# parameters
downsample = True
plot = True
save = True

im = np.array(Image.open("building.jpg"))

# Downsample by applying Average Pooling
if downsample:
    im = skimage.measure.block_reduce(im, (5,5,1), np.mean).astype(int)

orig_shape = im.shape

# flatten but keep RGB as features
im = im.reshape((-1,3))

# Without pooling, hierarchical clustering wouldn't work
# because it (supposedly) needs quadratic space
clf = KMeans()
preds = clf.fit_predict(im)

if plot:
    fig, (ax0, ax1) = plt.subplots(1,2, figsize=(12,6))

    ax0.imshow(im.reshape((orig_shape[0],orig_shape[1],3)))
    ax0.axis('off')
    ax1.imshow(preds.reshape((orig_shape[0],orig_shape[1])), )
    ax1.axis('off')

    plt.show()

    if save:
        fig.savefig("output.png")
