import customtkinter as ctk
import time
import threading

# Клас пральної машини
class WashingMachine:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.is_running = False

    def update_text(self, text):
        self.text_widget.insert('end', text + "\n")

    def fill_water(self):
        self.update_text("Заповнення водою...")
        time.sleep(3)
        self.update_text("Вода заповнена")

    def wash(self):
        self.update_text("Прання...")
        time.sleep(3)
        self.update_text("Прання завершено")

    def rinse(self):
        self.update_text("Полоскання...")
        time.sleep(3)
        self.update_text("Полоскання завершено")

    def spin(self):
        self.update_text("Віджимання...")
        time.sleep(3)
        self.update_text("Віджимання завершено")

    def run(self):
        self.is_running = True
        self.clear_text()
        self.update_text("Початок циклу прання.")
        self.fill_water()
        time.sleep(1.5)
        self.wash()
        time.sleep(1.5)
        self.rinse()
        time.sleep(1.5)
        self.spin()
        self.update_text("Цикл прання завершено.")
        self.is_running = False

    def clear_text(self):
        self.text_widget.delete("1.0", 'end')


def start_washing_machine(washing_machine):
    if not washing_machine.is_running:
        threading.Thread(target=washing_machine.run).start()
    else:
        print("Пральна машина вже запущена.")


# Створення вікна і всіх віджетів
app = ctk.CTk()
app.title("Симулятор пральної машини")
app.geometry("1920x1080")

custom_font = ctk.CTkFont(family="Arial", size=40)

text_box = ctk.CTkTextbox(app, width=800, height=800, font=custom_font)
text_box.pack(pady=20)

washing_machine = WashingMachine(text_widget=text_box)

start_button = ctk.CTkButton(app, text="Запустити пральну машину", font=custom_font, command=lambda: start_washing_machine(washing_machine))
start_button.pack(pady=20)

app.mainloop()
