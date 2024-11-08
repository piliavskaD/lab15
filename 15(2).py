import tkinter as tk

def action1():
    d = []
    input_text = t.get("1.0", tk.END)
    word = input_text.split()
    for i in word:
        if i not in d:
            d.append(i)
    res = " ".join(d)
    t.delete("1.0", tk.END)
    t.insert(tk.END, res) 

root = tk.Tk()
root.geometry("400x300")
root.title("Remove Repeated Words")

l = tk.Label(root, text="Input your text")
l.pack(pady=10)

t = tk.Text(root, width=40, height=10)
t.pack(padx=10, pady=10)

b = tk.Button(root, text="Remove Repeated Words", command=action1)
b.pack(pady=10)

root.mainloop()
