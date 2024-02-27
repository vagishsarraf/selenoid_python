#CONSTANTS
import inspect

URL = ""
USERNAME = "Admin"
PASSWORD = "admin123"


def whoami():
    return inspect.stack()[1][3]
