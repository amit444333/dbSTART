# Import the functions from the 'functions' module
from functions import add_job, update_job, delete_job, print_jobs

# Print a header for the list of jobs
print("The jobs: ")
print_jobs()
print()

# Prompt the user for an action ('A' to add, 'U' to update, 'D' to delete, 'S' to stop)
str = "Please press 'A' to add a job entry or press 'U' to update a job or 'D' to delete a job or 'S' to stop program: "
print(str)
func = input()
flag = True
while flag:

    # Add a new job
    if func == 'A':

        add_job()
        print(str)
        func = input()

    # Update an existing job
    elif func == 'U':

        update_job()
        print(str)
        func = input()

    # Delete a job
    elif func == 'D':

        delete_job()
        print(str)
        func = input()

    # Stop the program
    elif func == 'S':

        flag = False

    # Invalid input
    else:
        print("Invalid choice. Please try again.")
        break


