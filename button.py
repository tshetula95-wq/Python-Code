

import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        bmi_value.set("{:.2f}".format(bmi))
        if bmi < 18.5:
            category_value.set("Underweight")
        elif bmi >= 18.5 and bmi < 25:
            category_value.set("Normal weight. Congratulation, You are healthy")
        elif bmi >= 25 and bmi < 30:
            category_value.set("Overweight")
        else:
            category_value.set("Obesity")
    except ValueError:
        bmi_value.set("Error!")
        category_value.set("Sorry! Your Value in Incorrect")

def delete_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    category_label.config(text="")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("600x300")
root.configure (bg= "blue")


# Frame for inputs
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Height input

height_label = ttk.Label(input_frame, text="Enter your height (m):")
height_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
height_entry = ttk.Entry(input_frame)
height_entry.grid(row=0, column=1, padx=5, pady=5)


# Weight input
weight_label = ttk.Label(input_frame, text="Enter your weight (kg):")
weight_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
weight_entry = ttk.Entry(input_frame)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to calculate BMI
calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=5)

# Clear/Delet BMI
delete_button = ttk.Button(root, text="Delete Fields", command=delete_fields)
delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Frame for results
result_frame = ttk.Frame(root)
result_frame.pack(pady=10)

# Label to display BMI
bmi_label = ttk.Label(result_frame, text="Your BMI:")
bmi_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
bmi_value = tk.StringVar()
bmi_result = ttk.Label(result_frame, textvariable=bmi_value)
bmi_result.grid(row=0, column=1, padx=5, pady=5)

# Label to display BMI category
category_label = ttk.Label(result_frame, text="Category:")
category_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
category_value = tk.StringVar()
category_result = ttk.Label(result_frame, textvariable=category_value)
category_result.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
