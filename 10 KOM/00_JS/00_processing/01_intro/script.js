function setup(){
	createCanvas(500, 500);
	noStroke();
	console.log("Hello!")
}
function draw() {
	background(120);
	fill(255, 0, 0);
	ellipse(250, 250, 200, 200);

	fill(0, 255, 0, 160);
	ellipse(125, 250, 200, 200)

	fill(0, 0, 255, 160);
	ellipse(325, 250, 200, 200)
	console.log("Hello P5js!")
}