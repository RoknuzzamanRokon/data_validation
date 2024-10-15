import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_functions.mapping import create_json_file

if __name__ == "__main__":
    create_json_file()
