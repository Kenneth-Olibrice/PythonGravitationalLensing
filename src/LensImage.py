import matplotlib.image as mim
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import math
import scipy


# Capitalized variables are customizable constants
RADIUS = 115
LENS_X = 200
LENS_Y = 30
IMG_PATH = "../res/Lensed2.PNG"

img = mim.imread(IMG_PATH)
img_height, img_width = [img.shape[1], img.shape[0]] # img size

x_center = img_width / 2
y_center = img_height / 2


def radial_distortion(r, maximum):
    if r < maximum:
        return (maximum - r) * math.cos((math.pi * r) / (2 * maximum))
    else:
        return 0


def lens(a):
    x = a[0] - x_center
    y = a[1] - y_center

    # y is flipped due to +y pointing downwards by default
    # For our purposes, +x is right and +y is up
    mag = ((x-LENS_X)**2 + (y+LENS_Y)**2)**0.5

    if mag == 0:
        return 0, 0, a[2]

    if mag > RADIUS:
        return a[0], a[1], a[2]

    nx = x / mag
    ny = y / mag

    displacement = radial_distortion(mag, RADIUS)
    final_x = x + nx * displacement
    final_y = y + ny * displacement

    return final_x + x_center, final_y + y_center, a[2]


arr = np.asarray(img)
out = scipy.ndimage.geometric_transform(arr, lens)
plt.imshow(out)
plt.show()
