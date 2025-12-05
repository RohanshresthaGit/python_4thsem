from utils.exceptions.app_exception import InputException
from models.habit_mangaer import HabitManager

def display_menu():
    print("""
========== HABIT TRACKER ==========
1. Add Habit
2. View All Habits
3. Mark Progress
4. Show Streaks
5. Exit
===================================
""")


def main():
    try:
        manager = HabitManager()

        while True:
            display_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                manager.add_habit()
            elif choice == "2":
                manager.view_habits()
            elif choice == "3":
                manager.mark_progress()
            elif choice == "4":
                manager.view_streaks()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                raise InputException("Invalid input!")
    except InputException as e:
        print(e)


if __name__ == "__main__":
    main()
