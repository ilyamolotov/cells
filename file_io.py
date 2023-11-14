#file_io.py
# обработка файлов
from config import *



# получить путь изображения по номеру
def get_image_path_by_number(image_number):
    image_name = f"img ({image_number}).{IMAGE_EXTENSION}"
    image_path = os.path.join(IMAGE_FOLDER_PATH, image_name)
    return image_path

# загрузить изображение
def load_image(image_path):
    return Image.open(image_path)
