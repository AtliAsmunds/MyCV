let giftList = [];

function setup() {
  // create the canvas
  createCanvas(windowWidth, windowHeight);
  for (let i = 0; i < 60; i++) {
    let gift = new Gift(random(1,3), random(-100,100), random(-100,100));
    giftList.push(gift);
  }
}

function draw() {
  background(50, 100, 89);
  giftList.forEach(gift => {
    push();
    gift.move();
    translate(gift.x, gift.y)
    rotate(radians(gift.rotation_deg))
    gift.display();
    pop();
  })
}

class Gift {
  constructor(size, x_dir, y_dir) {
    this.velocity = createVector(x_dir, y_dir).normalize();
    this.width = this.height = 30 * size;
    this.x = random(this.width / 2, windowWidth - this.width / 2);
    this.y = random(this.height / 2, windowHeight - this.height / 2);
    this.rotation_deg = random(360);
    this.speed = random(0.5, 1);
    this.acc = 1;
  }

  move() {
    if ((this.x + this.width / 2) >= windowWidth || (this.x - this.width / 2) <= 0) {
        this.velocity.x *= -1;
    }
    if ((this.y + this.height / 2) >= windowHeight || (this.y - this.height / 2) <= 0) {
        this.velocity.y *= -1;
    }

    let mouseVector = createVector(mouseX, mouseY);
    let diff = createVector(this.x, this.y).sub(mouseVector)

    if (diff.mag() <= 60) {
      if (this.acc < 3) this.acc += 0.1;
      this.velocity = diff.normalize().mult(this.acc);
    } else if (this.acc > 1) {
      this.acc -= 0.01
      this.velocity = this.velocity.normalize().mult(this.acc)
    }
    this.x += this.velocity.x * this.speed;
    this.y += this.velocity.y * this.speed;
    
    this.rotation_deg = (this.rotation_deg + 0.1) % 360
  }
  
  display() {
    // ellipse(this.x, this.y, this.diameter, this.diameter)
    rectMode(CENTER);
    // translate(this.x + this.width/2, this.y + this.height/2)
    fill(30, 170, 80);
    stroke(1);
    // rotate(this.rotation)
    rect(0, 0, this.width, this.height)
    
    noStroke();
    fill(190, 70, 50)
    rect(0, 0, this.width, 10)
    rect(0, 0, 10, this.height)
  }
}