import re
from pathlib import Path
import sys


try:
    SEARCH_TAG = sys.argv[1]
except IndexError:
    SEARCH_TAG = "ID"

try:
    REVERSE_FLAG = bool(sys.argv[2])
except IndexError:
    REVERSE_FLAG = False


SORTED_LOG_FILE_NAME = f"sorted_log_rssi_{SEARCH_TAG}.txt"
LOG_FILE_NAME = "log_rssi.txt"
LOG_FILE_PATH = Path(__file__).parent / LOG_FILE_NAME
SORTED_LOG_FILE_PATH = Path(__file__).parent / SORTED_LOG_FILE_NAME


# remove sorted_log_file if it exists since we write to it with 'a' flag
if SORTED_LOG_FILE_PATH.is_file():
    SORTED_LOG_FILE_PATH.unlink()


PATTERN = rf".*{SEARCH_TAG} = (-?\d+)"


with open(LOG_FILE_NAME) as f:
    items_list = []
    while string := f.readline():
        parsing_item = re.match(PATTERN, string)
        if parsing_item:
            items_list.append(int(parsing_item.group(1)))


found_IDs = sorted(set(items_list), reverse=REVERSE_FLAG)  # only leave unique IDs

for ID in found_IDs:
    with open(LOG_FILE_NAME, "r") as f, open(SORTED_LOG_FILE_NAME, "a") as r:
        while string := f.readline():
            item = re.match(PATTERN, string)
            if item:
                item = item.group(1)
                item_id = int(item)
                if ID == item_id:
                    # print(f'{ID = }, {date = }, {string = }')		# debug
                    r.write(date)
                    r.write(string)
            else:
                date = string
