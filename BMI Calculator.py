#Import required packages
import tkinter as tk
from tkinter import messagebox, StringVar

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = float(feet_entry.get())
        inches = float(inches_entry.get())
        gender = gender_var.get()

        # Convert height from feet and inches to meters
        height_in_meters = (feet * 0.3048) + (inches * 0.0254)

        # Calculate BMI
        bmi = weight / (height_in_meters ** 2)

        # Interpret the BMI value based on gender
        if gender == "Male":
            if bmi < 20:
                weight_status = "You are underweight."
            elif bmi < 25:
                weight_status = "You have a normal weight."
            elif bmi < 30:
                weight_status = "You are overweight."
            else:
                weight_status = "You are obese."
        else:  # Female
            if bmi < 18.5:
                weight_status = "You are underweight."
            elif bmi < 24:
                weight_status = "You have a normal weight."
            elif bmi < 29:
                weight_status = "You are overweight."
            else:
                weight_status = "You are obese."

        # Display the result in a popup window
        result = f"Your BMI is: {bmi:.2f}\n{weight_status}"
        messagebox.showinfo("BMI Calculator", result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entry fields
weight_label = tk.Label(root, text="Enter your weight in kg:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

feet_label = tk.Label(root, text="Enter your height in feet:")
feet_label.pack()
feet_entry = tk.Entry(root)
feet_entry.pack()

inches_label = tk.Label(root, text="Enter your height in inches:")
inches_label.pack()
inches_entry = tk.Entry(root)
inches_entry.pack()

gender_label = tk.Label(root, text="Select your gender:")
gender_label.pack()
gender_var = StringVar()
gender_var.set("Male")  # Set a default option
gender_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_male.pack()
gender_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_female.pack()

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Run the main event loop
root.mainloop()