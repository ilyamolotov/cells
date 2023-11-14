#config.py

#==============================================================библиотеки
import numpy as np
import os
import tkinter as tk
from PIL import Image, ImageGrab, ImageTk


sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

#============================================================== параметры

# Путь к папке с изображениями
IMAGE_FOLDER_PATH = "img"
# Расширение файлов изображений
IMAGE_EXTENSION = "jpg"
# Выбранный номер изображения
chosen_image_number = 1  # Замените на нужный вам номер изображения

