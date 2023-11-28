# AI-digit-recognizer-with-custom-data-set-and-an-interface-in-python-tkinter


# Digit Recognizer ANN Project

![Digit Recognizer](./images/digitRecognizer.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction
This project is a simple, yet effective Artificial Neural Network (ANN) built using TensorFlow for digit recognition. It comes with an interactive interface that allows you to draw a digit, save it as a 50x50 BMP file, and predict the digit using the trained ANN model. The project also includes a Python script for extracting feature vectors from the drawn image and a script to find the smallest match vector[Source 0](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/).

## Features
- Custom dataset for training and testing.
- Digit drawing interface that saves images in BMP format.
- Python script to extract feature vectors by dividing the image array by 25 and calculating black pixels in each sub-matrix.
- ANN model built with TensorFlow.
- Python script for predicting digit from a given vector and finding the smallest match vector.
- Tkinter-based interface for drawing a digit and getting the prediction from the AI and the smallest match vector.

## Installation
To install and run this project, you will need Python and TensorFlow installed on your machine. Follow the steps below:

1. Clone the repository: `git clone https://github.com/rabah01abellache/AI-digit-recognizer-with-custom-data-set-and-an-interface-in-python-tkinter.git`
2. Navigate to the project directory: `cd AI-digit-recognizer-with-custom-data-set-and-an-interface-in-python-tkinter`
3. Install the necessary packages
4. Run file to make photos : `python createNumber.py`
4. Run file to extract the futuers vector : `python cara.py`
5. train the ai : `python tensorflow_train.py`
6. compare a vector to other vectors :  python Comapre.py
7. Interface to drow and get predictions : `python interface.py`

## Usage
After running the interface.py, you will see an interface where you can draw a digit. After drawing, click on "Predict" to get the prediction from the AI and the smallest match vector.

## License
This project is licensed under the terms of the MIT license.
