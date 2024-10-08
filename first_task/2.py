import customtkinter as ctk


# Функція для конвертування
def convert_distance():
    try:
        feet = float(entry.get())
        inches = feet * 12
        yards = feet * 0.333333333
        miles = feet * 0.000189393939
        result_label.configure(text=f"{feet} футів = {inches:.2f} дюймів\n"
                                    f"{yards:.2f} ярдів\n"
                                    f"{miles:.6f} миль")
    except ValueError:
        result_label.configure(text="Будь ласка, введіть правильне число")


# Створення вікна і всіх віджетів
app = ctk.CTk()
app.title("Конвертер відстані")
app.geometry("1280x1080")

custom_font = ctk.CTkFont(family="Arial", size=50)

entry_label = ctk.CTkLabel(app, text="Введіть відстань в футах:", font=custom_font)
entry_label.pack(pady=10)

entry = ctk.CTkEntry(app, font=custom_font, width=400, height=100)
entry.pack(pady=15)

convert_button = ctk.CTkButton(app, text="Конвертувати", command=convert_distance, font=custom_font)
convert_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=custom_font)
result_label.pack(pady=10)

app.mainloop()
