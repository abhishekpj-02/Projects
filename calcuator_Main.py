import tkinter as tk
import math  

def click(event):  # clickinte function
    current = display.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)  # Evaluate the current expression
            display.delete(0, tk.END)  # displayill ollath clear cheyyan
            display.insert(tk.END, result)  #reslut insert cheyyan
        except Exception:
            display.delete(0, tk.END)  #diplay clear cheyyan
            display.insert(tk.END, "Error")  # error ondengill error diplay cheyyan olath

    elif text == "C":
        display.delete(0, tk.END)  # display clear cheyyan
    elif text == "^":
        display.insert(tk.END, "**")
    elif text == "←":
        display.delete(len(current) - 1, tk.END)
    elif text == "n!":
        try:
            number = int(current)
            result = math.factorial(number)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "π":
        display.insert(tk.END, str(math.pi))
    else:
        display.insert(tk.END, text)  # displayilekk text insert cheyyan

#main application window
window = tk.Tk()
window.title("Calculator")
window.iconbitmap("c:/Users/abhis/Downloads/calculator-48_45851.ico")

# entry boxinte display
display = tk.Entry(window, font=("Arial", 20), justify="right", borderwidth=2, relief="solid")
display.pack(fill=tk.X, padx=10, pady=10, ipady=10)

# button frame
btn_frame = tk.Frame(window)
btn_frame.pack()

# Buttons
button_labels = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "π", "0", "n!", "/",
    "C", "=", "←", "^",
]

i = 0
for label in button_labels:
    if label == "=":
        button = tk.Button(btn_frame, text=label, font=("Arial", 13), padx=20, pady=20, bg="#4CAF50", fg="black")
    elif label == "C":
        button = tk.Button(btn_frame, text=label, font=("Arial", 13), padx=20, pady=20, bg="#f44336", fg="white")
    else:
        button = tk.Button(btn_frame, text=label, font=("Arial", 13), padx=20, pady=20, bg="#e0e0e0")
    button.grid(row=i // 4, column=i % 4, padx=10, pady=10)
    button.bind("<Button-1>", click)
    i += 1

window.mainloop()
