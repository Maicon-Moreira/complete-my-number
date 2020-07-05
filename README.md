# Complete My Number

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Complete my number é um programa em Python que utiliza um modelo de Inteligência artificial para prever a parte inferior de um número baseado na parte superior desenhada pelo usuário.

Demonstração: https://www.youtube.com/watch?v=WefbqdMbYso

Teste agora em: https://complete-meu-numero.vercel.app/

Google Colab: https://colab.research.google.com/drive/1Age5b0THNmzzt1glpwYbRAGGDpY1tfFJ

### Explicação técnica

![Latent Space Representation](https://miro.medium.com/max/3200/0*kHJ_LsPi-jz_CreZ.png)


Complete my number utiliza uma rede "Convolutional Encoder-Decoder", como mostrado na figura, no qual uma imagem é codificada em abstrações matemáticas e depois descodificada em uma nova imagem, no caso deste projeto, a parte superior do número é codificada, a representação simbólica é processada na rede neural e depois esses dados são transformados na parte inferior do número.

Detalhes mais avançados de como redes "Convolutional Encoder-Decoder" funcionam em: https://towardsdatascience.com/understanding-encoder-decoder-sequence-to-sequence-model-679e04af4346

Modelo utilizado neste projeto:

![Model used](https://i.ibb.co/X4rFR0Q/download-10.png)

### Uso

Crie o modelo:
```sh
$ python3 create_model.py
```

Treine o modelo:
```sh
$ python3 train_model.py
```

Teste o modelo:
```sh
$ python3 test_model.py
```

Converta o modelo para a versão JS 
```sh
$ sudo tensorflowjs_converter --input_format keras model.h5 webpage/model
```

Teste no seu navegador
```sh
$ http-server webpage -c-1 
```

**MIT**
**Free Software, Hell Yeah!**