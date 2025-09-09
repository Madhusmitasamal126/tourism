let score = 0;

document.addEventListener("DOMContentLoaded", () => {
	const container = document.getElementById("bubble-container");
	const maxBubbles = 20; // Limit to 20 bubbles

	setInterval(() => {
		if (container.children.length < maxBubbles) {
			createBubble();
		}
	}, 600);

	function createBubble() {
		const bubble = document.createElement("span");
		bubble.classList.add("bubbles");
		// Removed the line setting textContent to a Unicode character, didn't work very well

		const size = Math.random() * 3 + 2; // Random size between 2 and 5
		bubble.style.width = `${size}rem`;
		bubble.style.height = `${size}rem`;

		// Set the bubble background to the PNG image
		bubble.style.backgroundImage =
			"url('https://www.freepnglogos.com/uploads/bubbles/transparent-bubble-clip-art-creation-creatures-4.png')";
		bubble.style.backgroundSize = "contain"; // Ensure the image covers the bubble area
		bubble.style.backgroundRepeat = "no-repeat";
		bubble.style.backgroundPosition = "center";

		bubble.style.left = `${Math.random() * 100}%`; // Random horizontal start
		bubble.style.setProperty("--randomX", Math.random().toFixed(2)); // Set random X for translation

		container.appendChild(bubble);

		bubble.addEventListener("click", () => {
			bubble.classList.add("bubble-pop");
			setTimeout(() => bubble.remove(), 500); // Remove after pop animation

			// Increment score and update display
			score++;
			document.getElementById("score-counter").textContent = `Score: ${score}`;
		});
	}
});