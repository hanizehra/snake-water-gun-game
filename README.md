# 🐍 Snake, Water, Gun Game

A simple command-line **Snake, Water, Gun** game built with Python.

This beginner-friendly project was created to practice Python fundamentals such as user input, dictionaries, conditional statements, and the `random` module.

## 🎮 Game Rules

The game has three choices:

| Choice   | Value |
| -------- | ----: |
| 🐍 Snake |   `1` |
| 💧 Water |  `-1` |
| 🔫 Gun   |   `0` |

### Rules

* 🐍 Snake beats 💧 Water
* 💧 Water beats 🔫 Gun
* 🔫 Gun beats 🐍 Snake
* Same choice results in a **Draw**

## 🕹️ How to Play

When the game starts, enter one of the following:

```text
s → Snake
w → Water
g → Gun
```

The computer randomly selects a choice, and the program determines the winner based on the game rules.

## 📂 Project Structure

```text
snake-water-gun/
│
├── main.py
├── main-shortened.py
└── README.md
```

### `main.py`

Contains the game logic using individual `if`/`elif` conditions to handle the possible outcomes.

### `main-shortened.py`

Contains a simplified version of the game logic using numerical values to determine the winner.

Comments are included to explain the logic and make it easier to understand.

## 🧠 Concepts Practiced

* Variables and data types
* User input
* Dictionaries
* `if`, `elif`, and `else`
* Conditional logic
* Python `random` module
* Dictionary lookups
* Comparing values
* Simplifying program logic

## ▶️ How to Run

Make sure **Python** is installed on your computer.

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd snake-water-gun
```

Run the game:

```bash
python main.py
```

To run the shortened version:

```bash
python main-shortened.py
```

## 📌 Example

```text
-------- WELCOME TO SWG GAME --------
----------- GAME START -------------

Enter your choice: s

You Chose: Snake
Computer Chose: Water

You Win!
```

## 📚 Purpose

Practice

---

**Built with Python 🐍**
