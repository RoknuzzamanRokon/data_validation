import sys 
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_functions.mapping import update_content_value_with_providerHotelId

if __name__ == "__main__":
    update_content_value_with_providerHotelId()