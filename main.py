#main.py
from config import *
from interface import *
from img import *
from file_io import *

#===========================================================================================================выполнние MAIN

# Добавление кода для считывания и отображения изображения
image_path = get_image_path_by_number(chosen_image_number)  # Получаем путь к выбранному изображению
image = load_image(image_path)  # Загружаем изображение

# Вызов функции для отображения изображения по центру экрана
show_image_centered(image_path)
