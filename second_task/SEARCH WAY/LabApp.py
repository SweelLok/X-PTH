import customtkinter as ctk


class MazeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Maze Solver")
        self.geometry("400x500")

        self.labyrinth = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 1]
        ]
        # [1, 0, 0, 0],
        # [1, 0, 1, 0],
        # [0, 0, 0, 0],
        # [0, 1, 1, 1]

        # Створення шляху
        self.path = [[0 for _ in range(len(self.labyrinth[0]))] for _ in range(len(self.labyrinth))]

        self.create_widgets()

    def create_widgets(self):
        self.grid_frame = ctk.CTkFrame(self, width=400, height=400)
        self.grid_frame.pack(pady=10)

        self.solve_button = ctk.CTkButton(self, text="Find Path", command=self.find_ways)
        self.solve_button.pack(pady=10)

        # Створюємо сітку
        self.grid_cells = []
        for x in range(len(self.labyrinth)):
            row = []
            for y in range(len(self.labyrinth[0])):
                cell = ctk.CTkLabel(self.grid_frame, width=80, height=80, fg_color="white")
                cell.grid(row=x, column=y, padx=5, pady=5)
                row.append(cell)
            self.grid_cells.append(row)

        self.update_color()

    # Оновлення кольорів
    def update_color(self):
        for x in range(len(self.labyrinth)):
            for y in range(len(self.labyrinth[0])):
                color = "white" if self.labyrinth[x][y] == 1 else "black"
                self.grid_cells[x][y].configure(fg_color=color, text="")

    # Пошук шляху
    def solve_maze(self):
        queue = [(0, 0)]
        self.path[0][0] = 1

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            x, y = queue.pop(0)

            if x == len(self.labyrinth) - 1 and y == len(self.labyrinth[0]) - 1:
                return True

            for move in moves:
                new_x, new_y = x + move[0], y + move[1]

                if (0 <= new_x < len(self.labyrinth) and
                        0 <= new_y < len(self.labyrinth[0]) and
                        self.labyrinth[new_x][new_y] == 1 and
                        self.path[new_x][new_y] == 0):
                    queue.append((new_x, new_y))
                    self.path[new_x][new_y] = 1

        return False

    # Знаходження шляху та відображення його
    def find_ways(self):
        if self.solve_maze():
            for x in range(len(self.path)):
                for y in range(len(self.path[0])):
                    if self.path[x][y] == 1:
                        self.grid_cells[x][y].configure(fg_color="green")
        else:
            ctk.CTkLabel(self, text="No Path Found", fg_color="red").pack()


# Запуск додатку
if __name__ == "__main__":
    app = MazeApp()
    app.mainloop()

# len(self.labyrinth)     - визначає кількість рядків
# len(self.labyrinth[0])  - визначає кількість стовпців
# ^ 
# це для мене