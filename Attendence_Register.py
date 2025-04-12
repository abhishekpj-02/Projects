import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
from datetime import datetime
import pandas as pd

# Sample student list
students = ["Alice", "Bob", "Raj", "Sneha", "Kiran"]

# Attendance record
attendance_data = []

# Timetable + slot data (updated to match actual timetable)
timetable = {
    ("Monday", 1): "C", ("Monday", 2): "D", ("Monday", 3): "F", ("Monday", 4): "C", ("Monday", 5): "B", ("Monday", 6): "D", ("Monday", 7): "N",
    ("Tuesday", 1): "S/T", ("Tuesday", 2): "S/T", ("Tuesday", 3): "S/T", ("Tuesday", 4): "A", ("Tuesday", 5): "E", ("Tuesday", 6): "H/R(D)",
    ("Wednesday", 1): "A", ("Wednesday", 2): "B", ("Wednesday", 3): "C", ("Wednesday", 4): "S/T", ("Wednesday", 5): "S/T", ("Wednesday", 6): "S/T",
    ("Thursday", 1): "H/R(C)", ("Thursday", 2): "B(T)", ("Thursday", 3): "D", ("Thursday", 4): "F", ("Thursday", 5): "C(T)", ("Thursday", 6): "A(T)",
    ("Friday", 1): "D(T)", ("Friday", 2): "A", ("Friday", 3): "E", ("Friday", 4): "BREAK HOUR", ("Friday", 5): "H/R(D)", ("Friday", 6): "B"
}

# Updated slot details to exactly match timetable
slot_details = {
    "A": ("Discrete Mathematics", "Prince Achankunj"),
    "B": ("Computer Organization and Architecture", "Dr. Pradeep C,"),
    "C": ("Integrated Circuits", "Er. Ashly John, Er. Preena Pressa"),
    "D": ("Python for Machine Learning", "Er. Nishanth P.R."),
    "E": ("Professional Ethics", "Ms. Ann Mary Jacob"),
    "F": ("Constitution of India", "Ms. Vismaya Joy"),
    "S/T": ("Lab Session", "Integrated Circuits Lab: Er. Preena Pressa, Er. Pratap Pitkal | Python for ML Lab: Er. Nishanth P.R., Er. Ashwin P.V."),
    "H/R(C)": ("Integrated Circuits Revision", "Er. Ashly John"),
    "B(T)": ("Computer Organization Tutorial", "Dr. Pradeep C"),
    "C(T)": ("Integrated Circuits Tutorial", "Er. Preena Pressa"),
    "A(T)": ("Discrete Mathematics Tutorial", "Prince Achankunj"),
    "D(T)": ("Python for ML Tutorial", "Er. Nishanth P.R."),
    "H/R(D)": ("Python for ML Revision", "Er. Nishanth P.R."),
    "N": ("Python for ML Revision", "Er. Nishanth P.R."),
    "BREAK HOUR": ("No Class", "Break Time")
}

# UI setup
app = tk.Tk()
app.title("Individual Student Attendance")
style = Style("solar")

# Variables
date_var = tk.StringVar()
period_var = tk.StringVar()
selected_student = tk.StringVar()
attendance_status = tk.StringVar(value="Present")

slot_var = tk.StringVar()
subject_var = tk.StringVar()
faculty_var = tk.StringVar()

# Get weekday
def get_day(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%y")
        return date_obj.strftime("%A")
    except:
        return None

# Improved fetch_subject function
def fetch_subject():
    day = get_day(date_var.get())
    period = int(period_var.get()) if period_var.get().isdigit() else None
    
    if day and period:
        slot = timetable.get((day, period), "N/A")
        slot_var.set(slot)
        
        # Direct lookup for standard slots
        if slot in slot_details:
            subj, faculty = slot_details[slot]
            subject_var.set(subj)
            faculty_var.set(faculty)
        # Handle special cases
        elif slot == "S/T":
            # Determine which lab based on day
            if day == "Tuesday":
                subject_var.set("Python for ML Lab")
                faculty_var.set("Er. Nishanth P.R., Er. Ashwin P.V.")
            else:  # Wednesday
                subject_var.set("Integrated Circuits Lab")
                faculty_var.set("Er. Preena Pressa, Er. Pratap Pillai")
        else:
            subject_var.set("Unknown")
            faculty_var.set("Unknown")
    else:
        slot_var.set("Invalid")
        subject_var.set("")
        faculty_var.set("")

# Save student attendance
def save_attendance():
    student = selected_student.get()
    status = attendance_status.get()
    entry = {
        "Date": date_var.get(),
        "Day": get_day(date_var.get()),
        "Period": period_var.get(),
        "Slot": slot_var.get(),
        "Subject": subject_var.get(),
        "Faculty": faculty_var.get(),
        "Student": student,
        "Status": status
    }
    attendance_data.append(entry)
    print(f"Saved for {student}: {status}")
    
    # Optional: Save to CSV
    df = pd.DataFrame(attendance_data)
    df.to_csv("attendance_records.csv", index=False)

# --- Layout ---
main_frame = ttk.Frame(app, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Date and Period Input
ttk.Label(main_frame, text="Date (DD-MM-YY):").grid(row=0, column=0, sticky="e", pady=5)
ttk.Entry(main_frame, textvariable=date_var).grid(row=0, column=1, pady=5)

ttk.Label(main_frame, text="Period (1-7):").grid(row=1, column=0, sticky="e", pady=5)
ttk.Entry(main_frame, textvariable=period_var).grid(row=1, column=1, pady=5)

ttk.Button(main_frame, text="Fetch Subject", command=fetch_subject).grid(row=2, column=0, columnspan=2, pady=10)

# Subject Info Display
ttk.Label(main_frame, text="Slot:").grid(row=3, column=0, sticky="e", pady=5)
ttk.Label(main_frame, textvariable=slot_var).grid(row=3, column=1, sticky="w", pady=5)

ttk.Label(main_frame, text="Subject:").grid(row=4, column=0, sticky="e", pady=5)
ttk.Label(main_frame, textvariable=subject_var).grid(row=4, column=1, sticky="w", pady=5)

ttk.Label(main_frame, text="Faculty:").grid(row=5, column=0, sticky="e", pady=5)
ttk.Label(main_frame, textvariable=faculty_var).grid(row=5, column=1, sticky="w", pady=5)

# Student selector
ttk.Label(main_frame, text="Select Student:").grid(row=6, column=0, sticky="e", pady=5)
ttk.Combobox(main_frame, textvariable=selected_student, values=students).grid(row=6, column=1, pady=5)

# Attendance status
ttk.Label(main_frame, text="Attendance:").grid(row=7, column=0, sticky="e", pady=5)
ttk.Radiobutton(main_frame, text="Present", variable=attendance_status, value="Present").grid(row=7, column=1, sticky="w")
ttk.Radiobutton(main_frame, text="Absent", variable=attendance_status, value="Absent").grid(row=8, column=1, sticky="w")

ttk.Button(main_frame, text="Save Attendance", command=save_attendance).grid(row=9, column=0, columnspan=2, pady=20)

app.mainloop()