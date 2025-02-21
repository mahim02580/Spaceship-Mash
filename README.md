# Spaceship-Mash
Space Shooter Game

Overview

This is a simple Space Shooter game built using Python's turtle module. The player controls a spaceship that can move left and right while shooting at enemy spaceships. The goal is to destroy as many enemy spaceships as possible before any reach the bottom of the screen.

Features

Move the player spaceship using Left and Right arrow keys.

Shoot bullets using the Up arrow key.

Random enemy spaceships appear and move downward.

The game ends when an enemy spaceship reaches the bottom.

Score tracking system to count destroyed spaceships.

Technologies Used

Python

turtle module for graphics

time module for game loop management

random module for enemy spaceship spawning

How to Play

Run the main.py script.

Use the Left (←) and Right (→) arrow keys to move the spaceship.

Press the Up (↑) arrow key to shoot bullets.

Destroy enemy spaceships before they reach the bottom.

The game ends when an enemy spaceship reaches y < -280.

File Structure

📂 SpaceShooter
│── main.py          # Runs the game loop
│── player.py        # Handles player movement
│── gun.py           # Manages shooting mechanics
│── spaceship.py     # Controls enemy spaceship spawning and movement
│── scoreboard.py    # Displays score and game over text
│── spaceship_image.gif  # Image used for enemy spaceship (ensure this file exists)

Code Explanation

main.py

Initializes the game screen and player spaceship.

Listens for key events to move and shoot.

Manages game loop and collision detection.

player.py

Defines the Player class using the turtle module.

Implements move_right() and move_left() methods to move the spaceship.

gun.py

Defines the Gun class for shooting bullets.

Implements fire() to create bullets and move() to move them upward.

spaceship.py

Defines the Spaceship class to spawn and move enemy spaceships.

Implements create_spaceship() for random spawning and move() for movement.

scoreboard.py

Tracks and updates the player's score.

Displays a Game Over message when the game ends.

Possible Improvements

Add background music and sound effects.

Introduce multiple difficulty levels.

Implement power-ups and new enemy types.

Create a restart option after Game Over.

Author

Developed by Ethical Mahim

License

This project is open-source and can be modified or improved upon freely.

Happy coding and enjoy the game! 🎮🚀
