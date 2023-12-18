"""
docstring
"""
import time
class FileLogger:
    """
    docstring
    """
    filename = "log.txt"
    def write_message(self, message):
        """
        Append message to log file.
        """
        line = f"{int(time.time())} {message}\n"
        with open(self.filename, "a", encoding="utf-8") as outfile:
            outfile.write(line)

if __name__ == "__main__":
    logger = FileLogger()
    logger.write_message("Hello!")
