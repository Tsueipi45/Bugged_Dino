# Bugged_Dino (Python + Pygame)

This project is a simple yet challenging Dino game created with Python and Pygame, inspired by the classic Chrome Dino game. In this game, players control a dinosaur that must avoid obstacles like cacti and pterosaurs. The game becomes progressively harder as players advance, with obstacles increasing in speed.

## Features

- **Dynamic Obstacles**: Includes two types of obstacles—cacti and pterosaurs—that increase in speed over time.
- **Score Tracking**: Tracks and displays the score based on the number of obstacles passed.
- **Restart Mechanism**: Allows players to restart the game after losing.

## Installation

1. **Install Python**: Ensure Python 3.8+ is installed.
2. **Install Pygame**: Use pip to install Pygame.
   ```bash
   pip install pygame
   ```
3. **Download Assets**: Place game assets (images) in a folder named `Data`, in the same directory as the game script.
4. **Run the Game**: Execute the script in a terminal or IDE.
   ```bash
   python dino_game.py
   ```

## How to Play

- **Space or Up Arrow**: Jump to avoid obstacles.
- **Down Arrow**: Duck to avoid pterosaurs.
- **Objective**: Avoid obstacles as long as possible to score points.

## Project Structure

```plaintext
dino_game.py         # Main game code
Data/
├── Player.png       # Static player image
├── Player_1.png     # Running animation frame 1
├── Player_2.png     # Running animation frame 2
├── Cactus_1.png     # Cactus obstacle type 1
├── Cactus_2.png     # Cactus obstacle type 2
├── Pterosaur_1.png  # Pterosaur animation frame 1
├── Pterosaur_2.png  # Pterosaur animation frame 2
├── Ground.png       # Ground image
└── Cloud.png        # Cloud image for background
```

## License

This project is open-source and free to use.
