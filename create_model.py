import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Activation, Dropout, Reshape, UpSampling2D, Conv2DTranspose, Flatten

model = Sequential([
    Conv2D(filters=16, kernel_size=3, strides=2, padding='same', input_shape=(14, 28, 1)),
    Conv2D(filters=32, kernel_size=3, strides=2, padding='same'),
    Flatten(),
    Dense(100),
    Dropout(0.5),
    Dense(4*7*32),
    Reshape((4, 7, 32)),
    Conv2DTranspose(filters=16, kernel_size=3, strides=2, padding='same', activation='sigmoid'),
    Lambda(lambda x : x[:,1:,:]),
    Conv2DTranspose(filters=1, kernel_size=3, strides=2, padding='same', activation='sigmoid'),
])
model.summary()
model.compile('adam', 'mse')

model.save('model.h5')