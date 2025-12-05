class ProgressBar:
    @staticmethod
    def generate(progress, total, length=20):
        filled = int((progress / total) * length)
        return "[" + "#" * filled + "-" * (length - filled) + "]"
