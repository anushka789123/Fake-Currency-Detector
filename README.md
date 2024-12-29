Fake Currency Detector

Overview
The Fake Currency Detector is a machine learning-based application designed to detect fake ₹500 Indian Rupee notes. This project leverages a Convolutional Neural Network (CNN) model for image classification
and a Flask web framework for user interaction.The system uses a trained CNN model to differentiate between real and fake notes based on input images. Users can upload an image of a ₹500 note, and the system
will classify it as either "Real" or "Fake."

Libraries and Tools
The project utilizes the following libraries and tools:

1.Jupyter Notebook: For building and training the CNN model.
2.NumPy: For numerical computations.
3.Pillow (PIL): For image processing.
4.Matplotlib: For visualizing data.
5.OS: For managing file paths and directories.
6.TensorFlow and Keras: For building and training the CNN model.
7.Scikit-learn: For data preprocessing and evaluation metrics.
8.Flask: For creating the web interface.

Datasets
This currency detection system is specifically designed to work with Indian ₹500 notes. The dataset used for this project has been custom-built by collecting images of real and fake ₹500 notes from various
sources. These images are organized into appropriatecategories to facilitate effective training and evaluation of the model. For more details about the dataset and its preparation, refer to 
the project report included in this repository.

Project Structure
1.dataset/: Contains subfolders real and fake with labeled images.
2.templates/: Contains the index.html file for the web interface.
3.app.py: Flask application for loading the trained model and serving the web interface.
4.currentdetector.ipynb: Jupyter Notebook for building and training the CNN model

Working
Follow these steps to run the project:

Step 1:.Build and Train the CNN Model
1.Open the currentdetector.ipynb file in Jupyter Notebook.
2.Train the CNN model using the dataset.
3.Save the trained model to a file (e.g., model.h5).

Step 2: Setup Flask Application
1.Open app.py and update the paths to match the location of the saved model and dataset.
2.Load the trained model using TensorFlow/Keras in app.py.

Step 3:Run the Application
1.Start the Flask server by running the app.py file
2.Access the web interface by navigating to http://127.0.0.1:5000 in your web browser.

Step 4: Use the Detector
1.Upload an image of a ₹500 note via the web interface.
2.The system will classify the note as "Real" or "Fake".

That's all about project.






