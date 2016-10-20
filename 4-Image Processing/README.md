# Machine Learning - Image Processing
## Getting Started
You will require the following software:
* [Python](https://www.python.org/)
* [Anaconda (Recommended)](https://www.continuum.io/downloads)
* [SciKit-Learn](http://scikit-learn.org/stable/install.html)
* [SciKit-Image](http://scikit-image.org/download.html)

## Hackathon - Coins and Experiments

The coins.py code included is an example of how segmentation can be applied to images. The code step by step demonstrates how specific algorithms can be applied to segment the individual coins.

It is important to note that the algorithms work on a N-dimensional array. In the case of grayscale it is simply a 2D array with values 0 to 1 to represent darkness of the pixel. In the case of colour images, a 3 layered array is used to cater for RGB (Red, Green, Blue).

![Image Matrix](http://www.prolificidea.com/assets/img/ai/image_recognition-digit_matrix.png)

Here is an example of different filters being applied to the coins image.

![Image Processing](http://www.prolificidea.com/assets/img/ai/image_processing-coins.jpg)

**Experiment with the code and the SciKit Image API to segment the lena.jpg image. Share any interesting findings with everyone else at the hackathon.**

[SciKit Image Guides](http://scikit-image.org/docs/stable/auto_examples/index.html)

## Hackathon - Digit Classification

The digit_classification.py code included is an example of how a classifier can be trained to learn hand-written digits. It uses a base data set provided by SciKit.

Conceptually, image classification is almost no different to any other classification. The features of an image are the pixels that comprise the image instead of identified feature values. However, an image may contain numerous objects that may need to be segmented before identified correctly.

![Image Recognition](http://www.prolificidea.com/assets/img/ai/image_recognition-digits.png)

Interested in finding out more about digit classification? Try the [Tensor Flow tutorial](https://www.tensorflow.org/versions/r0.9/tutorials/mnist/beginners/index.html#mnist-for-ml-beginners)

## Libraries and languages

### SciKit Learn

Scikit learn is a python library with a whole range of different machine learning algorithms.  For Nueral Networks you can use the [Multi-Layer Perceptron](http://scikit-learn.org/dev/modules/neural_networks_supervised.html#classification)

### Java

Java developers can make use of [deeplearning4j](http://deeplearning4j.org/).  It is not as extensive as Scikit-Learn but it can be used for deep learning and Neural Networks.

### .Net

.Net developers can make use of [The Accord Framework](http://accord-framework.net/).  It is not as extensive as Scikit-Learn but has most of the libraries available and is quite easy to use.

### R

R can also be used for Neural Networks and an explanation of how to accomplish it you can have a look at [this blog post](https://www.r-bloggers.com/fitting-a-neural-network-in-r-neuralnet-package/)
