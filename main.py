import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Activation, Dropout, Reshape, UpSampling2D, Conv2DTranspose, Flatten
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

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

xs_test = []
ys_test = []
for image in tqdm(x_test):
    x = []
    y = []
    for line in image:
        if len(x) < 14:
            x.append(line)
        else:
            y.append(line)
    xs_test.append(x)
    ys_test.append(y)
xs_test = np.array(xs_test).reshape((10000, 14, 28, 1))/255
ys_test = np.array(ys_test).reshape((10000, 14, 28, 1))/255


model = Sequential([
    Conv2D(filters=16, kernel_size=3, strides=2, padding='same', input_shape=(14, 28, 1)),
    Conv2D(filters=32, kernel_size=3, strides=2, padding='same'),
    Flatten(),
    Dense(100),
    Dropout(0.3),
    Dense(7*14*32),
    Reshape((7, 14, 32)),
    Conv2DTranspose(filters=1, kernel_size=3, strides=2, padding='same', activation='sigmoid'),
])
model.summary()
model.compile('adam', 'mse')

# model.fit(xs, ys, epochs=5)

# for i in range(30):
#     plt.imshow(xs_test[i].reshape(14, 28))
#     plt.show()
#     plt.imshow(model.predict(np.array([xs_test[i]]))[0].reshape(14, 28))
#     plt.show()
#     plt.imshow(ys_test[i].reshape(14, 28))
#     plt.show()

# plt.imshow(xs_test[0].reshape(14, 28))
# plt.show()
# plt.imshow(model.predict(np.array([xs_test[0]]))[0].reshape(14, 28))
# plt.show()
# plt.imshow(ys_test[0].reshape(14, 28))
# plt.show()
