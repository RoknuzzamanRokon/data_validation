import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_functions.mapping import get_update_mapping_data_process
if __name__ == "__main__":
    get_update_mapping_data_process()

