# Cow Game

A game similar to the Google dinosaur game, where you play as a cow jumping over hay bales. This was my first pygame program, intended to familiarize myself with the library

## How It Works

- All objects, like the cow, hay bales, grass, ground, and health bar are represented as pygame rects and surfaces
- The cow is stationary while the ground moves under it, giving the illusion of the cow running
- When the cow collides with a haybale, the health decreases until the game is over
- The current score and high score are displayed on the left of the screen

## What I Learned

- Basics of Pygame
- rects and surfaces
- Game loop and keypress handling
- Rect collision
- Displaying text
- Loading images
- Basic game states
- Simulated gravity
