import tkinter as tk

def click(event):  #clickinte function
    current = display.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)  # Evaluate the current expression
            display.delete(0, tk.END)  # Clear the display
            display.insert(tk.END, result)  # Insert the result
        except Exception:
            display.delete(0, tk.END)  # Clear the display
            display.insert(tk.END, "Error")  # Insert "Error" if there's an exception

    elif text == "C":
        display.delete(0, tk.END)  # delete function use cheyth C click cheythal nammal enter cheytha entries okke delete aakum
    elif text == "^":
        display.insert(tk.END, "**")
    elif text == "←":
        display.delete(len(current)-1, tk.END)
    elif text in ["Sin", "Cos"]:
        display.delete(0, tk.END)
        display.insert(tk.END, "Chumma vechatha...:)")
    else:
        display.insert(tk.END, text)  # lefill number varaan tk.END inu pakaram 0 kodutha mathi

window = tk.Tk()
window.title("Calculator")
window.iconbitmap("c:/Users/abhis/Downloads/calculator-48_45851.ico")
display = tk.Entry(window, font=("Arial", 25), justify="right", borderwidth=2, relief="solid")
display.pack(fill=tk.X, padx=10, pady=10, ipady=10)

btn_frame = tk.Frame(window)
btn_frame.pack()

# Buttons
button_labels = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "Sin","0","Cos", "/", 
    "C","=", "←","^",
]

i = 0
for label in button_labels:
    if label == "=":
        button = tk.Button(btn_frame, text=label, font=("Arial", 18), padx=20, pady=20, bg="#4CAF50", fg="white")
    elif label == "C":
        button = tk.Button(btn_frame, text=label, font=("Arial", 18), padx=20, pady=20, bg="#f44336", fg="white")
    else:
        button = tk.Button(btn_frame, text=label, font=("Arial", 18), padx=20, pady=20, bg="#e0e0e0")
    button.grid(row=i//4, column=i%4, padx=10, pady=10)
    button.bind("<Button-1>", click)  # button click cheyumbo athinte value display cheyth varaan
    i += 1

window.mainloop()
