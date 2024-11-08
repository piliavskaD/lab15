import tkinter as tk

def draw_graph(canvas, data):
    canvas.delete("all") 

    width = 330
    height = 190
    margin = 20

    max_price = max(max(row) for row in data)
    x_step = (width - 2 * margin) / (len(data) - 1)
    y_step = (height - 2 * margin) / max_price

    canvas.create_line(margin, height - margin, width - margin, height - margin, arrow=tk.LAST)  # Вісь X
    canvas.create_line(margin, height - margin, margin, margin, arrow=tk.LAST)  # Вісь Y


    canvas.create_text(width - margin, height - margin + 10, text="Місяці")
    canvas.create_text(margin - 10, margin, text="Ціна", anchor="e")


    colors = ["red", "green", "blue"]
    labels = ["Хліб", "М'ясо", "Гречка"]

    for i in range(3):
        for j in range(len(data) - 1):
            x1 = margin + j * x_step
            y1 = height - margin - data[j][i] * y_step
            x2 = margin + (j + 1) * x_step
            y2 = height - margin - data[j + 1][i] * y_step
            canvas.create_line(x1, y1, x2, y2, fill=colors[i], width=2)
        
        canvas.create_text(width - margin - 50, margin + i * 15, text=labels[i], fill=colors[i])


def read_f(name):
    with open(name, "r", encoding="utf-8") as f:
        next(f)
        data = []
        for line in f:
            values = list(map(float, line.strip().split()[1:]))
            data.append(values)
        return data


file_name = "file.txt"
try:
    data = read_f(file_name)
except FileNotFoundError:
    print(f"Помилка: файл '{file_name}' не знайдено.")
    data = []

root = tk.Tk()
root.title("Графік цін")
root.geometry("330x190")
root["bg"] = "yellow"

canvas = tk.Canvas(root, width=300, height=150, bg="white")
canvas.grid(row=0, column=0, padx=15, pady=10)

btn = tk.Button(root, text="Побудувати графік", command=lambda: draw_graph(canvas, data))
btn.grid(row=1, column=0)

root.mainloop()
