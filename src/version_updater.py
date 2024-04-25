import datetime
import os.path
import re

from constants import ROOT_DIR


CONSTANT_PY_PATH = os.path.join(ROOT_DIR, "src", "constants.py")
PATTERN = r"VERSION: str = .+"
TODAY = datetime.datetime.now().strftime("%Y-%m-%d.%H")

REPLACE_BY = f'VERSION: str = "{TODAY}"'


# Open the file in read mode
with open(CONSTANT_PY_PATH) as file:
    lines = file.readlines()

# Check every line for the regular expression and replace it if found
for i in range(len(lines)):
    if re.match(PATTERN, lines[i]):
        if lines[i] != REPLACE_BY:
            lines[i] = REPLACE_BY + "\n"
        break

# Open the file again in write mode to save the changes
with open(CONSTANT_PY_PATH, "w") as file:
    file.writelines(lines)
