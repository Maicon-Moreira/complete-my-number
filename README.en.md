# Complete My Number

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Complete my number is a program in Python that uses an artificial intelligence model to predict the bottom of a number based on the top designed by the user.

Demonstration: https://www.youtube.com/watch?v=WefbqdMbYso
Test now at: https://complete-meu-numero.vercel.app/

### Technical explanation

![Latent Space Representation](https://miro.medium.com/max/3200/0*kHJ_LsPi-jz_CreZ.png)


Complete my number uses a "Convolutional Encoder-Decoder" network, as shown in the figure, in which an image is encoded in mathematical abstractions and then decoded into a new image, in the case of this project, the upper part of the number is encoded, the symbolic representation is processed in the neural network and then this data is transformed into the lower part of the number.

More advanced details on how Convolutional Encoder-Decoder networks work at: https://towardsdatascience.com/understanding-encoder-decoder-sequence-to-sequence-model-679e04af4346

Model used in this project:

![Model used](https://i.ibb.co/X4rFR0Q/download-10.png)

### How to Use

Create the model:
```sh
$ python3 create_model.py
```

Train the model:
```sh
$ python3 train_model.py
```

Test the model:
```sh
$ python3 test_model.py
```

Convert the model to the JS version 
```sh
$ sudo tensorflowjs_converter --input_format keras model.h5 webpage/model
```

Test in your browser
```sh
$ http-server webpage -c-1 
```

**MIT**
**Free Software, Hell Yeah!**