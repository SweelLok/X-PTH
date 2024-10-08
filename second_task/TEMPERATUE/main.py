# Імпорти
import customtkinter as ctk
from PIL import Image
from temperature_checker import check_temperature


# Створення гг вікна
app = ctk.CTk()
app.title("Temperature Checker")
app.geometry("800x800")

custom_font = ctk.CTkFont(family="Arial", size=25)

# Створення ентрі для вводу температури
entry = ctk.CTkEntry(app, placeholder_text="Введіть температуру (°C)", font=custom_font, width=310)
entry.pack(pady=10)

# Створення кнопок для перевірки
check_button = ctk.CTkButton(app, text="Перевірити", command=lambda: check_temperature(entry, result_label, image_label),
                             font=custom_font)
check_button.pack(pady=10)

# Створення лейбла для результату
result_label = ctk.CTkLabel(app, text=" ", font=custom_font)
result_label.pack(pady=10)

# Створення лейбла для фото
image_label = ctk.CTkLabel(app, text="")
image_label.pack(pady=10)

# Запуск програми
app.mainloop()
