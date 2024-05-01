# dino_pygame  

This is a Python implementation of the Chrome Dino Game using 
Model-View-Controller architecture. This version of the game takes in user 
camera inputs to detect jumps and crouches

## Getting Started

These instructions will get you up and running with a local version of the game
for development or testing purposes

### Prerequisites

- Python 3.8 or higher
- Pygame
- OpenCV
- MediaPipe

You can install the required packages using pip:

```sh
pip install -r requirements.txt
```

### Running the Game

To start the game, run the following command in your terminal:

```sh
python3 dino_game.py
```

### Game Controls

A calibration sequence and instructions will be displayed upon starting the program

- Use the `up` arrow key to make the dino jump or jump in real life if the camera is calibrated
- Use the `down` arrow key to make the dino duck or duck in real life if the camera is calibrated

### Running PyTests

To run unit tests, execute the following command in your terminal

```sh
pytest
```
