import tkinter as tk
from tkinter import messagebox, ttk  # Import the messagebox module
from functions import add_job, update_job, delete_job, print_jobs
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def add_job_gui():
    company = company_entry.get()
    name = name_entry.get()
    status = status_entry.get()

    # Validate input (you can add more validation logic here)
    if not company or not name or not status:
        messagebox.showerror("Error", "Please fill Company, Name and Status all fields.")
        return

    try:
        # Call the add_job function with the retrieved input
        add_job(company, name, status)
        messagebox.showinfo("Success", "Job added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def update_job_gui():
    job_uid = job_uid_entry.get()  # Retrieve the job UID from the input field
    new_status = new_status_entry.get()  # Retrieve the new status from the input field

    # Validate input (you can add more validation logic here)
    if not job_uid or not new_status:
        messagebox.showerror("Error", "Please fill in Job UID, New Status fields.")
        return

    try:
        # Call the update_job function with the retrieved input
        update_job(job_uid, new_status)
        messagebox.showinfo("Success", "Job updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def delete_job_gui():
    job_uid = job_uid_entry.get()  # Retrieve the job UID from the input field

    # Validate input (you can add more validation logic here)
    if not job_uid:
        messagebox.showerror("Error", "Please fill in Job UID field.")
        return

    try:
        # Call the delete_job function with the retrieved input
        delete_job(job_uid)
        messagebox.showinfo("Success", "Job deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def print_jobs_gui():
    # Create a new window for displaying job entries
    jobs_window = tk.Toplevel(root)
    jobs_window.title("Job Entries")

    # Create a text widget to display the job entries
    jobs_text = tk.Text(jobs_window, width=150, height=50)
    jobs_text.pack()

    # Retrieve job entries and insert them into the text widget
    jobs = print_jobs()  # Assuming print_jobs() returns a list of job entries
    for job in jobs:
        jobs_text.insert(tk.END, f"{job}\n")

def quit_app():
    root.quit()  # Close the entire application window

root = tk.Tk()
root.title("Job Management GUI")

# Set a custom font
custom_font = ("Cascadia Mono", 12)

# Create labels for each input field
company_label = ttk.Label(root, text="Company:", font=custom_font)
name_label = ttk.Label(root, text="Name:", font=custom_font)
status_label = ttk.Label(root, text="Status:", font=custom_font)
job_uid_label = ttk.Label(root, text="Job UID:", font=custom_font)
new_status_label = ttk.Label(root, text="New Status:", font=custom_font)

# Create Entry widgets for user input
company_entry = ttk.Entry(root, font=custom_font)
name_entry = ttk.Entry(root, font=custom_font)
status_entry = ttk.Entry(root, font=custom_font)
job_uid_entry = ttk.Entry(root, font=custom_font)
new_status_entry = ttk.Entry(root, font=custom_font)

# Pack the labels and Entry widgets
company_label.grid(row=0, column=0, padx=10, pady=5)
company_entry.grid(row=0, column=1, padx=10, pady=5)

name_label.grid(row=1, column=0, padx=10, pady=5)
name_entry.grid(row=1, column=1, padx=10, pady=5)

status_label.grid(row=2, column=0, padx=10, pady=5)
status_entry.grid(row=2, column=1, padx=10, pady=5)

job_uid_label.grid(row=3, column=0, padx=10, pady=5)
job_uid_entry.grid(row=3, column=1, padx=10, pady=5)

new_status_label.grid(row=4, column=0, padx=10, pady=5)
new_status_entry.grid(row=4, column=1, padx=10, pady=5)

# Create an "Add Job" button
add_button = ttk.Button(root, text="Add Job", command=add_job_gui, style="Accent.TButton")
add_button.grid(row=5, column=0, columnspan=2, pady=10)

update_button = ttk.Button(root, text="Update Job", command=update_job_gui, style="Accent.TButton")
update_button.grid(row=6, column=0, columnspan=2, pady=10)

delete_button = ttk.Button(root, text="Delete Job", command=delete_job_gui, style="Accent.TButton")
delete_button.grid(row=7, column=0, columnspan=2, pady=10)


# Create a button to print jobs
print_button = ttk.Button(root, text="Print Jobs", command=print_jobs_gui, style="Accent.TButton")
print_button.grid(row=9, column=0, columnspan=2, pady=10)

quit_button = ttk.Button(root, text="Quit", command=quit_app, style="Accent.TButton")
quit_button.grid(row=10, column=0, columnspan=2, pady=10)

# Set a custom style for buttons
style = ttk.Style()
style.configure("Accent.TButton", font=custom_font, background="#007ACC", foreground="black")

root.mainloop()
