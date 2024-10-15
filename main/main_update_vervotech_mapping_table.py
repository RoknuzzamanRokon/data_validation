import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_functions.mapping import update_vervotech_mapping_table
if __name__ == "__main__":
    update_vervotech_mapping_table()

