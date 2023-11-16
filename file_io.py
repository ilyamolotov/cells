#file_io.py
'''
1. открытие файла в директории 
2. обработка в массив (далее)
'''
from lib import *

def load_and_convert_to_gray(image_number):
    current_directory = os.getcwd()
    image_folder = os.path.join(current_directory, "img")
    filename = f"img ({image_number}).jpg"
    image_path = os.path.join(image_folder, filename)
    original_image = cv2.imread(image_path)