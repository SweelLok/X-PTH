# Імпорти
import customtkinter as ctk
from PIL import Image


# Функція для перевірки температури
def check_temperature(entry, result_label, image_label):
    try:
        temperature = float(entry.get())

        if temperature <= 0:
            message = "A cold, isn't it?"
            image_path = "photos/cold.png"
        elif 0 < temperature < 10:
            message = "Cool."
            image_path = "photos/cool.png"
        else:
            message = "Nice weather we're having."
            image_path = "photos/nice.png"

        result_label.configure(text=message)

        img = Image.open(image_path)
        img = img.resize((300, 300))
        photo = ctk.CTkImage(light_image=img, size=(300, 300))
        image_label.configure(image=photo)
        image_label.image = photo

    except ValueError:
        result_label.configure(text="Будь ласка, введіть числове значення.")
