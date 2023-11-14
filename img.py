# img.py
#обработка изображений


from config import *




#преобразовать изображение в массив
def image_to_array(image):
    return np.array(image)

#преобразовать массив в изображение
def array_to_image(image_array):
    return Image.fromarray(image_array)

