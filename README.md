# 🧠 ROSS MAZE Solver
### AIE111 – Artificial Intelligence Engineering  
**Final Project**


---

## 👥 Project Team

This project was developed by:

- Shaimaa Kotit
- Omar Elshaer

---


## 📌 Project Overview

**ROSS MAZE Solver** is an interactive, game-based AI application that visually demonstrates the **Breadth-First Search (BFS)** algorithm in action.  
The project allows users to design custom mazes, define start and goal positions, and observe how BFS systematically explores the maze to find the **shortest path**.

The application is built using **Python** and **Pygame**, focusing on algorithm visualization, user interaction, and real-time animation.

---

## 🎓 Course Information

- **Course Name:** Artificial Intelligence Engineering  
- **Course Code:** AIE111  
- **Institution:** Alamein International University  
- **Project Type:** Final Project  



---

## 🧩 Algorithm Explanation

### 🔹 What is Breadth-First Search (BFS)?

Breadth-First Search (BFS) is a graph traversal algorithm that explores all nodes at the current depth before moving to the next level.  
It guarantees finding the **shortest path** in unweighted graphs, making it ideal for maze-solving problems.

---

### 🔹 How BFS Works

1. Start position is added to a queue and marked as visited  
2. Repeatedly:
   - Dequeue the current cell
   - Check if it is the goal
   - Explore its 4 neighbors (up, down, left, right)
3. Valid, unvisited neighbors are:
   - Marked as visited
   - Assigned a parent cell
   - Added to the queue
4. Once the goal is reached, the shortest path is reconstructed using parent pointers

---

### 🔹 BFS Pseudocode

```text
BFS(grid, start, goal):
    queue ← start
    visited[start] ← true
    
    while queue not empty:
        current ← dequeue
        if current == goal:
            return path
        
        for each neighbor:
            if valid and not visited:
                visited ← true
                parent ← current
                enqueue neighbor
````

---

### 🔹 Why BFS is Optimal for Maze Solving

| Property                | Benefit                        |
| ----------------------- | ------------------------------ |
| Shortest Path Guarantee | Always finds minimum steps     |
| Completeness            | Finds a solution if one exists |
| Systematic Exploration  | Explores level by level        |
| Visual Clarity          | Easy to animate and understand |

---

### 🔹 Complexity Analysis

* **Time Complexity:** `O(V + E)`
* **Space Complexity:** `O(V)`
* Grid size: **15 × 16 = 240 cells**

---

## 🏗️ System Architecture

```
User Input (Mouse / Keyboard)
        ↓
main.py (Game Logic & Visualization)
        ↓
bfs.py (Pathfinding Algorithm)
        ↓
grid.py (Grid Management)
```

---

## 📂 Project Structure

```
ROSS-Maze-Solver/
│
├── main.py      # Game loop, GUI, animation, user input
├── bfs.py       # Breadth-First Search algorithm
├── grid.py      # Grid data and helper functions
├── README.md    # Project documentation
```

---

## 🧪 Game Controls

| Action      | Control           |
| ----------- | ----------------- |
| Draw Wall   | Left Mouse Click  |
| Remove Wall | Right Mouse Click |
| Set Start   | `S` key           |
| Set Goal    | `G` key           |
| Run BFS     | `SPACE`           |
| Reset Grid  | `R`               |
| Exit        | `ESC`             |

---

## 🎨 Visualization Color Guide

| Color  | Meaning             |
| ------ | ------------------- |
| White  | Empty Cell          |
| Black  | Wall                |
| Green  | Start Position      |
| Red    | Goal Position       |
| Blue   | Visited Cells       |
| Yellow | Final Shortest Path |

---

## 🖥️ Game Features

* Interactive maze creation
* Real-time BFS visualization
* Two-phase animation (exploration → solution path)
* Shortest path guarantee
* Statistics display (Visited cells & Path length)
* Clean and professional GUI

---

## 🚀 How to Run the Project

### Requirements

* Python 3.x
* Pygame

### Install Pygame

```bash
pip install pygame
```

### Run the Game

```bash
python main.py
```

---

## ✅ Project Status

* Algorithm Implementation: ✔️ Complete
* GUI & Visualization: ✔️ Complete
* Documentation: ✔️ Complete
* Testing & Validation: ✔️ Complete

---

## 📘 Learning Outcomes

* Practical understanding of BFS
* Real-time algorithm visualization
* Game-based AI learning approach
* Clean separation between logic, data, and UI

---

## 🏁 Final Notes

This project demonstrates how classical AI algorithms can be transformed into interactive learning tools.
ROSS MAZE Solver combines **theory, visualization, and user interaction** to deliver a clear and educational AI experience.

---

**© 2026 – AIE111 Final Project | Alamein International University**
