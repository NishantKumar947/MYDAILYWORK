from tkinter import *

# Function to perform the arithmetic operation
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operator.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result_label.config(text="Error: Division by zero")
            return
    else:
        result_label.config(text="Invalid Operation")
        return
    
    result_label.config(text=f"Result: {result}")

# Initialize the main window
win = Tk()
win.title("Simple Calculator")
win.geometry("300x400")

# Create and place the widgets
Label(win, text="Enter first number:").pack(pady=10)
entry_num1 = Entry(win)
entry_num1.pack(pady=5)

Label(win, text="Enter second number:").pack(pady=10)
entry_num2 = Entry(win)
entry_num2.pack(pady=5)

Label(win, text="Choose operation:").pack(pady=10)
operator = StringVar()
operator.set('+')  # Default value

Radiobutton(win, text="+", variable=operator, value='+').pack()
Radiobutton(win, text="-", variable=operator, value='-').pack()
Radiobutton(win, text="*", variable=operator, value='*').pack()
Radiobutton(win, text="/", variable=operator, value='/').pack()

Button(win, text="Calculate", command=calculate).pack(pady=20)

result_label = Label(win, text="Result: ", font=("Arial", 16))
result_label.pack(pady=10)

# Start the main loop
win.mainloop()
