import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Activation, Dropout, Reshape, UpSampling2D, Conv2DTranspose, Flatten
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

model = keras.models.load_model('model.h5')

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path="mnist.npz")

xs = []
ys = []
for image in tqdm(x_train):
    x = []
    y = []
    for line in image:
        if len(x) < 14:
            x.append(line)
        else:
            y.append(line)
    xs.append(x)
    ys.append(y)
xs = np.array(xs).reshape((60000, 14, 28, 1))/255
ys = np.array(ys).reshape((60000, 14, 28, 1))/255

for i in range(10):
  history = model.fit(xs, ys, epochs=3)

  model.save('model.h5')