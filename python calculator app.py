import tkinter as tk


window = tk.Tk()
window.title("Colorful Calculator")
window.geometry("340x500")
window.configure(bg="#1e1e2f")

entry = tk.Entry(
    window,
    width=18,
    font=("Arial", 24),
    borderwidth=0,
    justify="right",
    bg="#f8f8ff",
    fg="#222222"
)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=15, sticky="nsew")


def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(value))


def clear():
    entry.delete(0, tk.END)


def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")



number_bg = "#4ecca3"
operator_bg = "#ff9f43"
equal_bg = "#ee5253"
clear_bg = "#5f27cd"
text_color = "white"

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text.isdigit() or text == ".":
        bg_color = number_bg
        command = lambda t=text: click(t)
    elif text == "=":
        bg_color = equal_bg
        command = equal
    else:
        bg_color = operator_bg
        command = lambda t=text: click(t)

    btn = tk.Button(
        window,
        text=text,
        width=5,
        height=2,
        font=("Arial", 16, "bold"),
        bg=bg_color,
        fg=text_color,
        activebackground="#dcdde1",
        activeforeground="black",
        relief="flat",
        command=command
    )
    btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

clear_btn = tk.Button(
    window,
    text="C",
    font=("Arial", 16, "bold"),
    bg=clear_bg,
    fg="white",
    activebackground="#dcdde1",
    activeforeground="black",
    relief="flat",
    command=clear
)
clear_btn.grid(row=5, column=0, columnspan=4, padx=15, pady=15, sticky="nsew")


for i in range(6):
    window.grid_rowconfigure(i, weight=1)

for j in range(4):
    window.grid_columnconfigure(j, weight=1)

window.mainloop()
