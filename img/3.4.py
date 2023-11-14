# ======================================================================== библиотеки
import sys
import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import ttk

sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

# ======================================================================== Переменные пользователя
# Номер изображения
image_number = 1

# Начальные коэффициенты контрастности и порога яркости
initial_contrast_factor = 1.1
initial_brightness_threshold = 245

# Размеры большого изображения
large_image_width = 800
large_image_height = 600

# ======================================================================== Функции для обработки изображения
def process_image():
    global image_number, contrast_factor, brightness_threshold

    # Формирование имени файла
    filename = f"img ({image_number}).jpg"
    image_path = os.path.join(image_folder, filename)

    # Загрузка изображения
    original_image = cv2.imread(image_path)

    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Регулировка контрастности
    adjusted_image = cv2.convertScaleAbs(gray_image, alpha=contrast_factor, beta=0)

    # Бинаризация изображения с учётом порога яркости
    _, binary_image = cv2.threshold(adjusted_image, brightness_threshold, 255, cv2.THRESH_BINARY)

    # Поиск контуров на бинарном изображении
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Рисование границ объектов зелёным цветом на чёрно-белом изображении
    image_with_contours = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    # Изменение размеров изображения
    large_resized_image = cv2.resize(image_with_contours, (large_image_width, large_image_height))

    # Отображение результата
    cv2.imshow("Image with Contours", large_resized_image)

# ======================================================================== Создание GUI
root = tk.Tk()
root.title("Регулировка параметров")

# Инициализация переменных для меток и полей ввода
label_contrast = None
label_threshold = None
entry_image_number = None

def update_contrast(value):
    global contrast_factor, label_contrast
    contrast_factor = float(value)
    if label_contrast:
        label_contrast.config(text=f"Коэффициент контрастности: {contrast_factor:.2f}")
    process_image()

def update_threshold(value):
    global brightness_threshold, label_threshold
    brightness_threshold = int(float(value))  # Преобразование float в int
    if label_threshold:
        label_threshold.config(text=f"Порог яркости: {brightness_threshold}")
    process_image()

def update_image_number(event):
    global image_number
    new_image_number = entry_image_number.get()
    if new_image_number.isdigit():
        image_number = int(new_image_number)
        process_image()

def scale_image(event):
    global large_image_width, large_image_height
    delta = event.delta
    if delta > 0:
        large_image_width += 50
        large_image_height += 50
    elif delta < 0:
        large_image_width = max(50, large_image_width - 50)
        large_image_height = max(50, large_image_height - 50)
    process_image()

# ==============================================================Ползунки и метки для контрастности и порога яркости



# Слайдер порога яркости
slider_threshold = ttk.Scale(root, from_=255, to=100, length=300, orient="vertical", command=update_threshold)
slider_threshold.set(initial_brightness_threshold)
slider_threshold.grid(row=2, column=1, padx=10, pady=10)

# Метка для слайдера порога яркости
label_threshold = tk.Label(root, text=f"Порог яркости: {initial_brightness_threshold}")
label_threshold.grid(row=2, column=2, padx=10, pady=5)

# Слайдер коэффициента контрастности
slider_contrast = ttk.Scale(root, from_=2, to=0.1, length=300, orient="vertical", command=update_contrast)
slider_contrast.set(initial_contrast_factor)
slider_contrast.grid(row=2, column=3, padx=10, pady=10)

# Метка для слайдера коэффициента контрастности
label_contrast = tk.Label(root, text=f"Коэффициент контрастности: {initial_contrast_factor:.2f}")
label_contrast.grid(row=2, column=4, padx=10, pady=5)

# Поле ввода номера изображения
label_image_number = tk.Label(root, text="Номер изображения:")
label_image_number.grid(row=4, column=1, padx=10, pady=5)

# Поле ввода номера изображения
entry_image_number = tk.Entry(root)
entry_image_number.grid(row=5, column=1, padx=10, pady=5)
entry_image_number.insert(0, str(image_number))
entry_image_number.bind("<Return>", update_image_number)


# ======================================================================== Загрузка и обработка изображения

# Получение текущей директории
current_directory = os.getcwd()
image_folder = os.path.join(current_directory, "img")

# ========================Обработка изображения
process_image()

# ========================Обработка событий Tkinter
root.bind("<MouseWheel>", scale_image)
root.mainloop()
cv2.destroyAllWindows()
