from tkinter import *
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        dob = datetime(year, month, day)
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"Your age is: {age} years")
    except Exception as e:
        result_label.config(text="Invalid input. Please enter valid numbers.")

root = Tk()
root.title("Age Calculator")
root.geometry("350x250")

Label(root, text="Enter your Date of Birth", font=("Arial", 12, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=5)

Label(frame, text="Day:").grid(row=0, column=0, padx=5, pady=5)
day_entry = Entry(frame, width=5)
day_entry.grid(row=0, column=1, padx=5)

Label(frame, text="Month:").grid(row=0, column=2, padx=5, pady=5)
month_entry = Entry(frame, width=5)
month_entry.grid(row=0, column=3, padx=5)

Label(frame, text="Year:").grid(row=0, column=4, padx=5, pady=5)
year_entry = Entry(frame, width=8)
year_entry.grid(row=0, column=5, padx=5)

Button(root, text="Calculate Age", command=calculate_age, bg="#3895D3", fg="white").pack(pady=15)

result_label = Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()