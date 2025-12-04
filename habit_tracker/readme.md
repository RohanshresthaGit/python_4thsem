**Habit Progress Tracker (CLI App) - ROHAN SHRESTHA**
    The Habit Progress Tracker is a command-line based productivity tool designed to help users build and maintain good habits.
    Using a beautiful ASCII progress bar system and streak tracking logic, this project provides a simple yet engaging way to stay consistent every day.

    This project uses Python, OOP, JSON-based storage, and provides a clean modular structure — perfect for real life usage.

**Features**
  1. Add new habits
     - Create habits like “Exercise”, “Coding”, “Reading”, etc., and set daily goals.

  2. Mark daily progress
     - Log your daily effort and visually track it using ASCII progress bars.

  3. Daily streak tracking
     - Automatically keeps count of how many consecutive days you have worked on each habit.

  4. View all habits
     - Displays progress bars and progress numbers clearly for each habit.

  5. JSON storage
     - Your habits and progress are stored locally inside a JSON file (data/habits.json).

  6. CLI based
     - No GUI needed — can operate inside the terminal.


📂 Project Structure

    habit_tracker/
    │
    ├── main.py                     # Entry point of program/ App.
    │
    ├── models/
    │   ├── habit.py                # Habit class
    │   ├── progress_bar.py         # ASCII Progress Bar class
    │   └── habit_manager.py        # Logic for habit management
    │
    ├── data/
    │   └── habits.json             # JSON storage
    │
    └── README.md                   # Documentation

**💻 Getting the Project On Your Local Computer**
    Follow the steps below to clone and run this project:

    Step 1: Install Git(If Git is not installed):
        Windows: download from git-scm.com
        Mac/Linux: already installed usually

    Step 2: Clone the Repository
        Open Terminal or CMD and run:
        git clone https://github.com/<your-username>/habit-tracker.git
        Replace <your-username> with your real GitHub username.
        This will download the project folder onto your computer.

    Step 3: Navigate into the Project
        cd habit-tracker

**▶️ Running the Application**
    Once inside the project directory, simply run:
    type "python main.py" on your terminal.

And you are ready to goo!!🔥

--Rohan Shrestha