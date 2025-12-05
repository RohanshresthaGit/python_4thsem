class Habit:
    def __init__(self, name, goal, progress=0, streak=0, last_marked=None):
        self.name = name
        self.goal = goal
        self.progress = progress
        self.streak = streak
        self.last_marked = last_marked

    def to_dict(self):
        return {
            "name": self.name,
            "goal": self.goal,
            "progress": self.progress,
            "streak": self.streak,
            "last_marked": self.last_marked
        }
