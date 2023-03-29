document.addEventListener("DOMContentLoaded", () => {
	let canvas = document.getElementById("canvas");
	let ctx = canvas.getContext("2d");

	const blockSize = 20;
	const column = canvas.width / blockSize
	// const column = canvas.width / 20;
	const row = column;
	// const blockSize = canvas.width / column;

	let score = 0;
	let start = false;

	// console.log(column, row, blockSize, canvas.width, canvas.height);

	//Object Border
	let border = {
		color : "Black",
		size  : blockSize,
		height : canvas.height,
		width : canvas.width,

		draw : function () {
			ctx.fillStyle = this.color;
			const top = ctx.fillRect(0, 0, this.width, this.size);
			const right = ctx.fillRect(this.width-this.size, 0, this.size, this.height);
			const bottom = ctx.fillRect(0, this.height-this.size, this.width, this.size);
			const left = ctx.fillRect(0, 0, this.size, this.height);
		}
	}

	let scoreText = {
		font : "20px Courier",
		color : "White",
		align : "left",
		baseline : "top",

		draw : function () {
			let x = 14;
			let y = 14;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align
			ctx.textBaseLine = this.baseline;
			ctx.fillText(`Score: ${score}`, x, y);
		}
	}

	const startButton = {
		x : canvas.width / 2,
		y : canvas.height / 2 ,
		width : 6 * blockSize,
		height : 2 * blockSize,
		color : "Black",
		textColor : "White",
		font : "32px Courier",
		align : "center",
		baseline : "middle",

		draw : function () {
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x - this.width/2, this.y - this.height/2, this.width, this.height);

			ctx.fillStyle = this.textColor;
			ctx.font = this.font;
			ctx.textAlign = this.align;
			ctx.textBaseLine = this.baseline;
			ctx.fillText('Start', this.x, this.y);
		},
		checkClicked : function (event) {
			if ((event.offsetX >= this.x - this.width/2) && (event.offsetY >= this.y - this.height/2) && (event.offsetX <= (this.x+this.width/2)) && (event.offsetY <= (this.y+this.height/2))) start = true;
		}
	}

	const gameoverText = {
		font : "60px Courier",
		color : "Black",
		align : "center",
		baseline : "middle",

		draw : function () {
			clearInterval(mainloop);
			let x = (canvas.width / 2) - 175;
			let y = canvas.height / 2;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textBaseLine = this.baseline;
			ctx.fillText(`Game Over!`, x, y);
		}
	}

	//Object Block
	class Block{
		constructor (row, column){
			this.row = row;
			this.column = column;
			this.size = blockSize;
		}
		circle(x, y, radius, color, isFilled){
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI, false);
			ctx.closePath();
			if (isFilled){
				ctx.fillStyle = color;
				ctx.fill();
			}
		}
		drawSquare(color){
			let x = this.column * blockSize;
			let y = this.row * blockSize
			this.color = color;

			ctx.fillStyle = this.color;
			ctx.fillRect(x, y, this.size, this.size);
		}
		drawCircle(color){
			let x = this.column * blockSize + blockSize / 2;
			let y = this.row * blockSize + blockSize / 2;
			this.color = color;

			this.circle(x, y, this.size / 2, this.color, true);
		}
	}

	class Snake{
		constructor() {
			this.segments = [
			new Block(7,5), //head
			new Block(6,5),
			new Block(5,5) //tail
			]
			this.direction = "right";
			this.nextDirection = "right";
		}

		draw() {
			this.segments.forEach( (segment) =>{
				segment.drawSquare("Green")
			} )
		}

		setDirection(newDirection){
			this.nextDirection = newDirection;
			if (this.direction === "up" && newDirection === "down") return;
			else if (this.direction === "down" && newDirection === "up") return;
			else if (this.direction === "left" && newDirection === "right") return;
			else if (this.direction === "right" && newDirection === "left") return;
			// console.log(newDirection)
			this.nextDirection = newDirection;
		}

		move(){
			let head = this.segments[0];
			let newHead;

			this.direction = this.nextDirection;

			if (this.direction === "right") newHead = new Block(head.row, head.column+1);
			else if (this.direction === "down") newHead = new Block(head.row+1, head.column);
			else if (this.direction === "left") newHead = new Block(head.row, head.column-1);
			else if (this.direction === "up") newHead = new Block(head.row-1, head.column);

			if (this.checkCollision(newHead)) {
			 	gameoverText.draw();
			 	return;
			}

			this.segments.unshift(newHead);
			//this.segments.pop()

			if (this.eatApple(head)){
				score++;
				apple.move();
			} else {
				this.segments.pop()
			}

		}
		checkCollision(head){
			const leftCollision = head.column === 0;
			const topCollision = head.row === 0;
			const rightColision = head.column === column - 1;
			const bottomCollision = head.row === row -1;

			const wallCollision = leftCollision || topCollision || rightColision || bottomCollision;

			this.segments.forEach((segment, i) =>{
				// console.log()
				if (head.row === segment.row && head.column == segment.column){
					const selfCollision = true;
					return selfCollision

				}
			});
			return wallCollision
		}

		eatApple(head){
			if (head.row == apple.block.row && head.column == apple.block.column) {
				return true;
			}
			return false;
		}
	}

	class Apple{
		constructor() {
			this.block = new Block(0, 0);

			this.move();
		}

		draw(){
			this.block.drawCircle("Red");
		}

		move(){
			let randomRow = Math.floor(Math.random() * (row -2)) + 1;
			let randomColumn = Math.floor(Math.random() * (column -2)) + 1;
			this.block.row = randomRow;
			this.block.column = randomColumn;
		}
	}

	// border.draw();
	// scoreText.draw();
	// gameoverText.draw()

	 let snake = new Snake();
	// snake.draw();

	 let apple = new Apple();
	// apple.draw();

	// basic movement (i really need to know all its secret to harvest the potential to its limit)

	// document.querySelector("body").onkeydown = (event) => {
	//	console.log(event.code); (all kind of event in body) (toward object)
	//}

	// $('body').keydown( (event) -> {
	// 	console.log(event.keyCode);
	// })

	let mainloop = setInterval( () => {
			ctx.clearRect(0, 0, canvas.width, canvas.height);
			border.draw();
			scoreText.draw();
			snake.draw();
			apple.draw();
			if (start){
				snake.move();
			} else {
				startButton.draw();
			}
		}, 100)

	document.addEventListener('keydown', () => {
		// console.log(event.code) //(toward any event)
		switch (event.code){
			case "ArrowUp":
				// console.log("Up!")
				snake.setDirection("up");
				break;
			case "ArrowDown":
				// console.log("Down!")
				snake.setDirection("down")
				break;
			case "ArrowLeft":
				// console.log("Left!")
				snake.setDirection("left")
				break;
			case "ArrowRight":
				// console.log("Right!")
				snake.setDirection("right")
				break;
			default:
				// console.log("nope.")
		}
	})

	document.querySelector("#canvas").addEventListener('click', function(event){
		startButton.checkClicked(event);
	})
})