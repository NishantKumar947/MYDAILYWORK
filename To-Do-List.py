from tkinter import *
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to clear all tasks
def clear_tasks():
    tasks_listbox.delete(0, END)

# Function to update a selected task
def update_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        new_task = task_entry.get()
        if new_task != "":
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    else:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Function to select a task for updating
def select_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task_entry.delete(0, END)
        selected_task = tasks_listbox.get(selected_task_index)
        task_entry.insert(0, selected_task)
    else:
        messagebox.showwarning("Warning", "You must select a task.")

# Initialize the main window
win = Tk()
win.title("To-Do List Application")
win.geometry("400x500")

# Create and place the widgets
task_label = Label(win, text="Enter Task:", font=("Arial", 14))
task_label.pack(pady=10)

task_entry = Entry(win, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Create a frame for the task management buttons
button_frame = Frame(win)
button_frame.pack(pady=10)

add_button = Button(button_frame, text="Add Task", width=10, font=("Arial", 14), command=add_task)
add_button.pack(side=LEFT, padx=5)

select_button = Button(button_frame, text="Select Task", width=10, font=("Arial", 14), command=select_task)
select_button.pack(side=LEFT, padx=5)

update_button = Button(button_frame, text="Update Task", width=15, font=("Arial", 14), command=update_task)
update_button.pack(side=LEFT, padx=5)

# Create and place the listbox for tasks
tasks_listbox = Listbox(win, width=40, height=10, font=("Arial", 14), selectmode=SINGLE)
tasks_listbox.pack(pady=20)

# Create a frame for the delete and clear buttons
manage_frame = Frame(win)
manage_frame.pack(pady=10)

delete_button = Button(manage_frame, text="Delete Task", width=12, font=("Arial", 14), command=delete_task)
delete_button.pack(side=LEFT, padx=5)

clear_button = Button(manage_frame, text="Clear All Tasks", width=12, font=("Arial", 14), command=clear_tasks)
clear_button.pack(side=LEFT, padx=5)

# Start the main loop
win.mainloop()
