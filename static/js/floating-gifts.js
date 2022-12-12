let giftList = [];

function setup() {
  // create the canvas
  createCanvas(windowWidth, windowHeight);
  for (let i = 0; i < 30; i++) {
    let gift = new Gift(random(2,4), random(-100,100), random(-100,100));
    giftList.push(gift);
  }
}

function draw() {
  background(50, 100, 89);
  giftList.forEach(gift => {
    gift.move();
    gift.display();
  })
}

class Gift {
  constructor(size, x_dir, y_dir) {
    this.velocity = createVector(x_dir, y_dir).normalize();
    this.width = this.height = 30 * size;
    this.x = random(this.width / 2, windowWidth - this.width / 2);
    this.y = random(this.height / 2, windowHeight - this.height / 2);
    this.rotation = radians(random(360));
    this.speed = random(0.5, 1);
  }

  move() {
    if ((this.x + this.width / 2) >= windowWidth || (this.x - this.width / 2) <= 0) {
        this.velocity.x *= -1;
    }
    if ((this.y + this.height / 2) >= windowHeight || (this.y - this.height / 2) <= 0) {
        this.velocity.y *= -1;
    }

    this.x += this.velocity.x * this.speed;
    this.y += this.velocity.y * this.speed;
  }
  
  display() {
    // ellipse(this.x, this.y, this.diameter, this.diameter)
    rectMode(CENTER);
    fill(30, 170, 80);
    stroke(1);
    rect(this.x, this.y, this.width, this.height)
    
    noStroke();
    fill(190, 70, 50)
    rect(this.x, this.y, this.width, 10)
    rect(this.x, this.y, 10, this.height)
  }
}