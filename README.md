# Decision-Making Game

A simple console-based decision-making game implemented in Python.

## How to Play

The game presents a list of friends, enemies, and buttons. Your goal is to make decisions that affect your health and score based on the encountered elements.

- Friends increase your health but decrease your score.
- Enemies decrease your health but increase your score.
- Buttons trigger a transformation, turning all friends into enemies or vice versa.

## Game Rules

1. You start with 10 health points and a score of 0.
2. Interact with the encountered element by choosing either to interact (1) or ignore (2).
3. Your health and score will be adjusted based on your decision.
4. The game continues until your health reaches 0 or the list is empty.

## Example Interaction

Game list: [0, 1, 2, 0, 1, 2, 1, 2, 0, 1]
There are 4 friends and 4 enemies
Your health is 10
Your score is 0
You see a friend
1 - Interact
2 - Ignore
What will you do? 1
Your health increased to 12, but your score decreased to -1.
...
