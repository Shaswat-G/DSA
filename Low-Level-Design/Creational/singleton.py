@singleton
class Logger:
    def __init__(self):
        self.log_file = open("app.log", "a")
        self.log_level = "INFO"

    def log(self, message, level="INFO"):
        if self._should_log(level):
            self.log_file.write(f"[{level}] {message}\n")
            self.log_file.flush()

    def _should_log(self, level):
        levels = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}
        return levels.get(level, 1) >= levels.get(self.log_level, 1)


# Usage throughout application
logger = Logger()
logger.log("Application started")
