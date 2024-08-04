import os
import tkinter as tk
from tkinter import messagebox, ttk  # Import the messagebox module
from functions import DBConn, DBJobs
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class MainApplication(tk.Frame):
    def __init__(self, parent:tk.Tk, dbj:DBJobs, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.dbj = dbj

        self.parent.title("Job Management GUI")

        # Set a custom font
        custom_font = ("Cascadia Mono", 12)

        # Create labels for each input field
        self.company_label = ttk.Label(self.parent, text="Company:", font=custom_font)
        self.name_label = ttk.Label(self.parent, text="Name:", font=custom_font)
        self.status_label = ttk.Label(self.parent, text="Status:", font=custom_font)
        self.job_uid_label = ttk.Label(self.parent, text="Job UID:", font=custom_font)
        self.new_status_label = ttk.Label(self.parent, text="New Status:", font=custom_font)

        # Create Entry widgets for user input
        self.company_entry = ttk.Entry(self.parent, font=custom_font)
        self.name_entry = ttk.Entry(self.parent, font=custom_font)
        self.status_entry = ttk.Entry(self.parent, font=custom_font)
        self.job_uid_entry = ttk.Entry(self.parent, font=custom_font)
        self.new_status_entry = ttk.Entry(self.parent, font=custom_font)

        # Pack the labels and Entry widgets
        self.company_label.grid(row=0, column=0, padx=10, pady=5)
        self.company_entry.grid(row=0, column=1, padx=10, pady=5)

        self.name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.status_label.grid(row=2, column=0, padx=10, pady=5)
        self.status_entry.grid(row=2, column=1, padx=10, pady=5)

        self.job_uid_label.grid(row=3, column=0, padx=10, pady=5)
        self.job_uid_entry.grid(row=3, column=1, padx=10, pady=5)

        self.new_status_label.grid(row=4, column=0, padx=10, pady=5)
        self.new_status_entry.grid(row=4, column=1, padx=10, pady=5)

        # Create an "Add Job" button
        add_button = ttk.Button(self.parent, text="Add Job", command=self.add_job_gui, style="Accent.TButton")
        add_button.grid(row=5, column=0, columnspan=2, pady=10)

        update_button = ttk.Button(self.parent, text="Update Job", command=self.update_job_gui, style="Accent.TButton")
        update_button.grid(row=6, column=0, columnspan=2, pady=10)

        delete_button = ttk.Button(self.parent, text="Delete Job", command=self.delete_job_gui, style="Accent.TButton")
        delete_button.grid(row=7, column=0, columnspan=2, pady=10)


        # Create a button to print jobs
        print_button = ttk.Button(self.parent, text="Print Jobs", command=self.print_jobs_gui, style="Accent.TButton")
        print_button.grid(row=9, column=0, columnspan=2, pady=10)

        quit_button = ttk.Button(self.parent, text="Quit", command=self.quit_app, style="Accent.TButton")
        quit_button.grid(row=10, column=0, columnspan=2, pady=10)

        # Set a custom style for buttons
        style = ttk.Style()
        style.configure("Accent.TButton", font=custom_font, background="#007ACC", foreground="black")

    def add_job_gui(self):
        company = self.company_entry.get()
        name = self.name_entry.get()
        status = self.status_entry.get()

        # Validate input (you can add more validation logic here)
        if not company or not name or not status:
            messagebox.showerror("Error", "Please fill Company, Name and Status all fields.")
            return

        try:
            # Call the add_job function with the retrieved input
            self.dbj.add_job(company, name, status)
            messagebox.showinfo("Success", "Job added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update_job_gui(self):
        job_uid = self.job_uid_entry.get()  # Retrieve the job UID from the input field
        new_status = self.new_status_entry.get()  # Retrieve the new status from the input field

        # Validate input (you can add more validation logic here)
        if not job_uid or not new_status:
            messagebox.showerror("Error", "Please fill in Job UID, New Status fields.")
            return

        try:
            # Call the update_job function with the retrieved input
            self.dbj.update_job(job_uid, new_status)
            messagebox.showinfo("Success", "Job updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def delete_job_gui(self):
        job_uid = self.job_uid_entry.get()  # Retrieve the job UID from the input field

        # Validate input (you can add more validation logic here)
        if not job_uid:
            messagebox.showerror("Error", "Please fill in Job UID field.")
            return

        try:
            # Call the delete_job function with the retrieved input
            self.dbj.delete_job(job_uid)
            messagebox.showinfo("Success", "Job deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def print_jobs_gui(self):
        # Create a new window for displaying job entries
        jobs_window = tk.Toplevel(self.parent)
        jobs_window.title("Job Entries")

        # Create a text widget to display the job entries
        jobs_text = tk.Text(jobs_window, width=150, height=50)
        jobs_text.pack()

        # Retrieve job entries and insert them into the text widget
        jobs = self.dbj.print_jobs()  # Assuming print_jobs() returns a list of job entries
        for job in jobs:
            jobs_text.insert(tk.END, f"{job}\n")

    def quit_app(self):
        self.parent.quit()  # Close the entire application window

if __name__ == "__main__":
    conn = DBConn(host=os.environ['HOST'], dbname=os.environ['DBNAME'], user=os.environ['USER'], password=os.environ['PASSWORD'], port=os.environ['PORT'])
    root = tk.Tk()
    MainApplication(root, DBJobs(conn, os.environ['CSV_PATH']))
    root.mainloop()
    conn.close()
