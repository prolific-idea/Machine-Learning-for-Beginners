import numpy as np
import skimage
from skimage import data, io, filters
from skimage.feature import canny
from scipy import ndimage as ndi
from skimage.filters import sobel
from skimage.morphology import watershed

# Load coins image data
image = data.coins()
image = skimage.io.imread('Dataset/lena.jpg',flatten=True)
io.imshow(image)
io.show()

# Find edges with the Sobel algorithm
sobelEdges = filters.sobel(image)
io.imshow(sobelEdges)
io.show()

# Find edges with the Canny algorithm
cannyEdges = edges = canny(image/255.)
io.imshow(cannyEdges)
io.show()

# Fill holes in the edges found with the Canny algorithm
fill_coins = ndi.binary_fill_holes(cannyEdges)
io.imshow(fill_coins)
io.show()

# Highlight the extremes of the image
markers = np.zeros_like(image)
markers[image < 30] = 1
markers[image > 150] = 2

# Follow the gradient of the image to fill gaps
segmentation = watershed(sobelEdges, markers)
segmentation = ndi.binary_fill_holes(segmentation - 1)

labeled_coins, _ = ndi.label(segmentation)

io.imshow(labeled_coins)
io.show()