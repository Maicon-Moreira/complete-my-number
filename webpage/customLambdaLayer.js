// Essa camada do modelo teve que ser escrita a mão,
// pois a versão Javascript do Tensorflow não suporta nativamente

class LambdaRemoveFirstSubTensor extends tf.layers.Layer {
  constructor() {
    super({});
    this.supportsMasking = true;
  }

  computeOutputShape(inputShape) {
    return [inputShape[0], inputShape[1] - 1, inputShape[2], inputShape[3]]
  }

  call(inputs, kwargs) {
    let input = inputs;
    if (Array.isArray(input)) {
      input = input[0];
    }
    this.invokeCallHook(inputs, kwargs);

    const subTensors = tf.unstack(input, 1)
    subTensors.shift()
    const output = tf.stack(subTensors, 1)
    return output
  }

  static get className() {
    return 'LambdaRemoveFirstSubTensor';
  }
}
tf.serialization.registerClass(LambdaRemoveFirstSubTensor)