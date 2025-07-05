# Python Chess Game ♟️

A complete chess game built in Python using **Pygame**, demonstrating object-oriented programming principles, user interaction, and rule-based gameplay mechanics.

> AI mode under development 🤖

---

## 🧠 Key Highlights

- ♟️ Full-featured chessboard with legal move validation
- 🔁 Restartable games
- 🎨 Theme toggling (Green, Brown, Blue, Gray)
- 🖱️ Drag-and-drop functionality
- 🏰 Special moves: Castling
- 🗃️ Organized modular codebase using OOP

---

## 🧰 Tech Stack

- **Language:** Python
- **Graphics Engine:** Pygame

---

## 📁 Project Structure

chess-game-py/
├── src/
│ ├── main.py # Game entry point
│ ├── game.py # Turn handling & board rendering
│ ├── board.py # Game logic: moves, rules
│ ├── piece.py # Piece definitions & movement
│ ├── dragger.py # Drag-and-drop handler
│ ├── config.py # Game settings
│ ├── theme.py, color.py# Themes and UI styles
├── assets/
│ ├── images/ # Piece images (multiple themes)
│ └── sounds/ # Move and capture sounds
├── snapshots/ # Game screenshots
└── README.md


---

## 🎮 How to Play

Clone the repository:
git clone https://github.com/ajaysurya07/chess-game-py.git
cd chess-game-py


Install dependencies:
pip install pygame

Run the game:
python src/main.py

🕹️ Controls
Drag a piece to move it

Press t to change board themes (Green, Brown, Blue, Gray)

Press r to restart the game
