import sys
import os
from main_functions.mapping import get_update_mapping_data_process

# Add the parent directory to the system path so Python can find main_functions
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    get_update_mapping_data_process()
