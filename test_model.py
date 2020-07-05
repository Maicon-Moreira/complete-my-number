import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

model = keras.models.load_model('model.h5')

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path="mnist.npz")

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

for i in range(30):
    top = xs_test[i].reshape(14, 28)
    bottom_true = ys_test[i].reshape(14, 28)

    x = np.array([top.reshape(14, 28, 1)])
    y = model.predict(x)[0].reshape(14, 28)

    img1 = np.array([*top, *y])
    img2 = np.array([*top, *bottom_true])

    plt.imshow(img1)
    plt.show()
    plt.imshow(img2)
    plt.show()