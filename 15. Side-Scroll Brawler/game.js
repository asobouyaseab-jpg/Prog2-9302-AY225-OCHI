// Player object
class Player {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.width = 50;
    this.height = 80;
    this.state = "idle"; // idle, attack, run, jump, etc.
    this.comboStep = 0;
    this.attackCooldown = false;
  }

  update(keys) {
    // Movement logic
    if (keys["ArrowRight"]) {
      this.x += 5;
      this.state = "run";
    } else if (keys["ArrowLeft"]) {
      this.x -= 5;
      this.state = "run";
    } else {
      if (this.state !== "attack") this.state = "idle";
    }
  }

  attack(enemies) {
    if (this.attackCooldown) return;
    this.state = "attack";
    this.comboStep = (this.comboStep + 1) % 3; // 3-hit combo
    this.attackCooldown = true;

    // Generate hitbox
    const hitbox = {
      x: this.x + this.width,
      y: this.y,
      width: 40,
      height: this.height
    };

    enemies.forEach(enemy => {
      if (this.checkCollision(hitbox, enemy)) {
        enemy.takeDamage(10);
      }
    });

    // End attack after a short delay
    setTimeout(() => {
      this.attackCooldown = false;
      this.state = "idle";
    }, 300);
  }

  checkCollision(a, b) {
    return (
      a.x < b.x + b.width &&
      a.x + a.width > b.x &&
      a.y < b.y + b.height &&
      a.y + a.height > b.y
    );
  }
}

// Enemy object
class Enemy {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.width = 50;
    this.height = 80;
    this.hp = 30;
  }

  takeDamage(amount) {
    this.hp -= amount;
    if (this.hp <= 0) {
      console.log("Enemy defeated!");
    }
  }
}
