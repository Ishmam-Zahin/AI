from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from keras.datasets import mnist
import cv2
import matplotlib.pyplot as plt

EPOCHS = 10
IMG_WIDTH = 28
IMG_HEIGHT = 28

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# x_train = cv2.resize(x_train, (IMG_WIDTH, IMG_HEIGHT))
# x_test = cv2.resize(x_test, (IMG_WIDTH, IMG_HEIGHT))
# print(x_train[0].shape)

model = Sequential([
    Input(shape=(IMG_WIDTH, IMG_HEIGHT, 1)),
    Conv2D(32, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=EPOCHS)
model.evaluate(x_test, y_test, verbose=2)