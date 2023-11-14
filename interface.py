#interface.py
# интерфейс окна, отображений и т.д.


from config import *

#вывести изображение по центру
def show_image_centered(image_path):
    root = tk.Tk()
    root.title("Отображение изображения")

    # Загрузка изображения
    image = Image.open(image_path)
    
    # Изменение размера изображения на 800x600
    image = image.resize((800, 600), Image.BICUBIC)

    # Преобразование изображения для использования в Tkinter
    photo = ImageTk.PhotoImage(image)

    # Создание виджета Label для отображения изображения
    label = tk.Label(root, image=photo)
    label.pack()

    # Функция для закрытия окна по крестику
    def on_closing():
        root.destroy()

    # Переопределение действия при закрытии окна через крестик
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Получение размеров экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Вычисление координат для позиционирования окна по центру экрана
    window_width = 800  # Ширина окна
    window_height = 600  # Высота окна
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2

    # Установка позиции окна на экране
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Запуск основного цикла обработки событий Tkinter
    root.mainloop()
