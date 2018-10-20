# Point-and-Image-Classification
Classifying points and images using the nearest neighbour classifier


Getting Started

  Platforms (built on):-
    1. Ubuntu 18.04.1 LTS Bionic Beaver
    2. Anaconda Navigator
    3. Jupyter Notebook
    
  Installing:-
    1. To download and install Ubuntu (different versions) - https://www.ubuntu.com/download/desktop
    2. To download Anaconda - https://www.anaconda.com/download/#download
    3. To install Anaconda - http://docs.anaconda.com/anaconda/install/linux/
    4. Jupyter Notebook is available on Anaconda Navigator for download
    
  Using Anaconda:-
    In the Linux command-line, type "anaconda-navigator" to open Anaconda Navigator
    
  Learning Source:-
    edX - https://cs50.harvard.edu/
  

About the Project

This machine-learning project comprises of python code fragments which are used to classify points and images.
The project makes use of the nearest-neighbour classifier algorithm for the above mentioned purpose.

  Point Classification:-
    A graph is plotted containing six points. These points are divided into two groups of three points each. Each group is assigned a colour - one red and the other green. A new test point is defined. The output of the program is the colour of the group to which the new point belongs.
    The test point is classified based on the smallest distance of a predefined point from the test point.
    
  
  Image Classification:-
    
    The image classification module consists of three code fragments:
      The first program works with a single image.
      The second program analyzes the errors occuring when the same program is used to classify 100 images.
      The third program improves the performance and runs the program for 100 images.
      
    1. The first program:-
      The digits dataset is imported and a training set of first 10 images of the digits dataset is created.
      Next, a test image is created and the nearest-neighbour classifier algorithm is run to classify the image. The correct output is displayed.
      
    2. The second program:-
      The number of images to be classified is increased from 1 to 100 and it is found that 63 outputs are correct and 37 are wrong. This error is analyzed.
      
    3. The third program:-
      The training set is increased from 10 images to 1000 images and the same program is run. The program displays 97 correct outputs and three wrong ones. The performance of the project is increased.


Author
  Shekhar Raha
  Github Profile - https://github.com/ShekharRaha
