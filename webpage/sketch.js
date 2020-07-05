const ws = 300
const gridSize = 28
const quadSize = ws / gridSize
let grid = []
let model
let empty = false

async function loadModel() {
  model = await tf.loadLayersModel('./model/model.json');

  model.summary()
}
loadModel()

function setup() {
  createCanvas(ws, ws);

  const footer = document.createElement('h2')
  footer.innerHTML = 'Made by <a target="blank" href="https://www.linkedin.com/in/maicon-moreira-38ab691a4/">Maicon</a> with ❤️'
  document.body.appendChild(footer)

  reset()
}

function draw() {


  if (model) {
    // console.log(model.predict)
  }

  if (mouseIsPressed && mouseX > 0 && mouseX < ws && mouseY > 0 && mouseY < ws / 2) {
    setEmpty()

    const x = Math.floor(mouseX / quadSize)
    const y = Math.floor(mouseY / quadSize)

    for (let quadX = 0; quadX < gridSize; quadX++) {
      for (let quadY = 0; quadY < gridSize / 2; quadY++) {
        const distance = dist(x, y, quadX, quadY)
        if (distance < 1.3) {
          let value = 1
          if (value > 1) value = 1
          if (value < 0) value = 0
          if (grid[quadY][quadX] < 1) {
            noStroke()
            grid[quadY][quadX][0] += value
            if (grid[quadY][quadX][0] > 1) grid[quadY][quadX][0] = 1
            if (grid[quadY][quadX][0] < 0) grid[quadY][quadX][0] = 0

            stroke(255 - grid[quadY][quadX][0] * 255)
            fill(255 - grid[quadY][quadX][0] * 255)
            rect(quadX * quadSize, quadY * quadSize, quadSize, quadSize)

          }
        }
      }
    }
  }
}

function setEmpty() {
  if (empty) {
    empty = false

    background(255)
  }
}

setInterval(() => {
  if (!empty) {

    const x = tf.tensor4d([grid])
    const y = model.predict(x).arraySync()[0]

    noStroke()
    fill(255)
    rect(0, ws / 2, ws, ws / 2)

    for (iLine in y) {
      _line = y[iLine]
      for (iPixel in _line) {
        pixel = _line[iPixel][0]

        fill(255 - pixel * 255)
        stroke(255 - pixel * 255)

        rect(iPixel * quadSize, iLine * quadSize + ws / 2, quadSize, quadSize)
      }
    }
  }
}, 50)

function update() {
  empty = setEmpty()
  for (let quadX = 0; quadX < gridSize; quadX++) {
    for (let quadY = 0; quadY < gridSize / 2; quadY++) {
      stroke(255 - grid[quadY][quadX][0] * 255)
      fill(255 - grid[quadY][quadX][0] * 255)
      rect(quadX * quadSize, quadY * quadSize, quadSize, quadSize)
    }
  }
}

function reset() {
  if (!empty) {

    empty = true
    textAlign(CENTER, CENTER)
    textSize(20)
    background(255)
    fill(0)

    text('Desenhe aqui a parte\n superior de um número...', ws / 2, ws / 4)
    text('...e eu completarei\n a parte de baixo aqui,\n como mágica 🤗', ws / 2, 3 * ws / 4)

    stroke(0)
    line(0, ws / 2, ws, ws / 2)

    for (let y = 0; y < gridSize / 2; y++) {
      grid[y] = []
      for (let x = 0; x < gridSize; x++) {
        grid[y][x] = [0]
      }
    }
  }
}
document.getElementById('_clear').onclick = reset

document.getElementsByTagName('canvas')[0].onclick = e => {
  e.preventDefault()
}