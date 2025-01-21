"""
Author: Aidan Kiser
Version: 30 October 2024
"""

import logging
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, linear_model
import pandas as pd
import numpy as np
import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Configure logging
logging.basicConfig(
    filename='w10_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def readData():
    try:
        logging.info("Reading Iris dataset.")
        iris = datasets.load_iris()
        X = iris.data
        Y = iris.target
        df = pd.DataFrame(X, columns=iris.feature_names)
        logging.info("Dataset loaded successfully. Shape: %s", df.shape)
        return df
    except Exception as e:
        logging.error("Error reading Iris dataset: %s", e)

def makePrediction():
    try:
        logging.info("Initiating KNN prediction.")
        iris = datasets.load_iris()
        knn = KNeighborsClassifier(n_neighbors=6)
        knn.fit(iris['data'], iris['target'])
        X = [
            [5.9, 1.0, 5.1, 1.8],
            [3.4, 2.0, 1.1, 4.8],
        ]
        prediction = knn.predict(X)
        logging.info("Prediction made: %s", prediction)
    except Exception as e:
        logging.error("Error during KNN prediction: %s", e)

def doRegression():
    try:
        logging.info("Performing linear regression on diabetes dataset.")
        diabetes = datasets.load_diabetes()
        diabetes_X = diabetes.data[:, np.newaxis, 2]
        diabetes_X_train = diabetes_X[:-20]
        diabetes_X_test = diabetes_X[-20:]
        diabetes_y_train = diabetes.target[:-20]
        diabetes_y_test = diabetes.target[-20:]
        regr = linear_model.LinearRegression()
        regr.fit(diabetes_X_train, diabetes_y_train)
        diabetes_y_pred = regr.predict(diabetes_X_test)
        logging.info("Linear regression completed.")
    except Exception as e:
        logging.error("Error during regression: %s", e)

def doDeepLearning():
    try:
        logging.info("Starting deep learning model training.")
        train_images = mnist.train_images()
        train_labels = mnist.train_labels()
        test_images = mnist.test_images()
        test_labels = mnist.test_labels()

        train_images = (train_images / 255) - 0.5
        test_images = (test_images / 255) - 0.5

        train_images = np.expand_dims(train_images, axis=3)
        test_images = np.expand_dims(test_images, axis=3)

        model = Sequential([
            Conv2D(8, 3, input_shape=(28, 28, 1)),
            MaxPooling2D(pool_size=2),
            Flatten(),
            Dense(10, activation='softmax'),
        ])

        model.compile('adam', loss='categorical_crossentropy', metrics=['accuracy'])

        model.fit(
            train_images,
            to_categorical(train_labels),
            epochs=3,
            validation_data=(test_images, to_categorical(test_labels)),
        )

        model.save_weights('cnn.h5')
        predictions = model.predict(test_images[:5])
        logging.info("Model predictions: %s", np.argmax(predictions, axis=1))
        logging.info("Actual labels: %s", test_labels[:5])
    except Exception as e:
        logging.error("Error during deep learning: %s", e)

if __name__ == '__main__':
    logging.info("Script started.")
    try:
        data_frame = readData()
        makePrediction()
        doRegression()
        doDeepLearning()
        logging.info("Script completed successfully.")
    except Exception as e:
        logging.error("An error occurred in the main script: %s", e)
