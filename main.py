# main.py 

from lib import *

# Удаление шумов с изображения

    denoised_image = cv2.medianBlur(image, int(median_kernel_size))
    return denoised_image



# Бинаризация изображения


# Поиск и отрисовка контуров на изображении
def find_and_draw_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_with_contours = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)
    return image_with_contours

# Отображение обработанного изображения с контурами
def display_processed_image(image):
    large_image_width = 800
    large_image_height = 600
    large_resized_image = cv2.resize(image, (large_image_width, large_image_height))
    cv2.imshow("Image with Contours", large_resized_image)

# Основная функция обработки изображения
def process_image():
    gray_image = load_and_convert_to_gray(image_number)
    denoised_image = remove_noise(gray_image)
    adjusted_image = adjust_contrast(denoised_image, initial_contrast_factor)
    binary_image = binarize_image(adjusted_image, initial_brightness_threshold)
    image_with_contours = find_and_draw_contours(binary_image)
    display_processed_image(image_with_contours)

process_image()
cv2.waitKey(0)
cv2.destroyAllWindows()
