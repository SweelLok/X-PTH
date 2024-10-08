#Імпорти
import customtkinter as ctk

from labyrinth import labyrinth


# Клас для відображення лабіринту
class LabyrinthApp(ctk.CTk):
    def __init__(self, **kwargs):
        self.title("Labyrinth ways")
        self.geometry("800x800")

        self.labyrinth = labyrinth

        self.create_widgets()

        def create_widgets(self):
            pass

        def find_ways(self):
            pass

        def upgrade_color(self):
            pass

        def reset_color(self):
            pass

        def is_way(self):
            pass

        def solve_labyrinth(self):
            pass

