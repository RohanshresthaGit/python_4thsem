import json
import os
from datetime import datetime
from models.habit import Habit
from models.progress_bar import ProgressBar

DATA_FILE = "data/habits.json"


class HabitManager:

    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

        self.habits = self.load_habits()

    def load_habits(self):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Habit(**h) for h in data]

    def save_habits(self):
        with open(DATA_FILE, "w") as f:
            json.dump([h.to_dict() for h in self.habits], f, indent=4)

    def add_habit(self):
        name = input("Habit name: ")
        goal = int(input("Daily goal (e.g., minutes): "))

        self.habits.append(Habit(name, goal))
        self.save_habits()
        print("Habit added!\n")

    def view_habits(self):
        if not self.habits:
            print("No habits yet!\n")
            return

        print("\n===== Your Habits =====")
        for habit in self.habits:
            bar = ProgressBar.generate(habit.progress, habit.goal)
            print(f"{habit.name}: {bar} ({habit.progress}/{habit.goal})")
        print()

    def mark_progress(self):
        name = input("Which habit did you work on? ")

        for habit in self.habits:
            if habit.name == name:
                minutes = int(input("How many minutes today? "))
                habit.progress += minutes

                today = datetime.now().strftime("%Y-%m-%d")

                if habit.last_marked == today:
                    pass
                else:
                    habit.streak += 1

                habit.last_marked = today

                if habit.progress > habit.goal:
                    habit.progress = habit.goal

                self.save_habits()
                print("Progress updated!\n")
                return

        print("Habit not found!\n")

    def view_streaks(self):
        print("\n===== Streaks =====")
        for habit in self.habits:
            print(f"{habit.name}: 🔥 {habit.streak} day streak")
        print()
