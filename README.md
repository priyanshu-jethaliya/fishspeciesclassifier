# Fish Species Classifier Web App


## Overview

The Fish Species Classifier is a web application built to predict the species of common fish based on their physical characteristics. The application utilizes a machine learning model trained on a dataset containing fish species along with their corresponding weight, length, height, and width measurements. Users can input the physical attributes of a fish through the user-friendly web interface and receive real-time predictions about the species.

## Demo

[Link to Live Demo](https://fish-species-classifier-0e4abdc0791b.herokuapp.com/)

## Features

- Interactive web interface to input fish measurements and obtain species predictions.
- Utilizes a pre-trained machine learning model to provide accurate and efficient predictions.
- Supports a variety of common fish species for classification.
- Easy-to-use and visually appealing frontend design.
- Deployed on Heroku for easy accessibility.

## Built With

- Python
- Flask (backend framework)
- HTML, CSS, JavaScript (frontend)
- Scikit-learn (machine learning model)
- Gunicorn (WSGI server)
- Heroku (deployment)

## How to Use

1. Go to the [Live Demo](https://fish-species-classifier-0e4abdc0791b.herokuapp.com/) link.

2. Enter the measurements of the fish species you want to classify.

3. Click the "Predict" button to obtain the predicted species.

4. The application will display the predicted species based on the provided measurements.

## Installation and Local Setup

To run the web application locally, follow these steps:

1. Clone the repository to your local machine.

2. Navigate to the project directory.

3. Create a virtual environment and activate it.

4. Install the required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
