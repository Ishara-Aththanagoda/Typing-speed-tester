from tkinter import *
import time

# create Initialize the main window
root = Tk()
root.title("Typing Speed Tester")
root.geometry("600x400")
root.configure(background='lightblue')

# create Sample string for testing typing speed
test_string = "Python is an interpreted, high-level programming language"
word_count = len(test_string.split())
border = '-+-' * 10

# Create labels to show instructions and results
instruction_label = Label(root, text="Type the given phrase as fast as possible:", font=("Helvetica", 14), bg='lightblue')
instruction_label.pack(pady=10)

phrase_label = Label(root, text=test_string, font=("Helvetica", 12, "italic"), wraplength=500, bg='lightblue')
phrase_label.pack(pady=10)

# create Entry box for user input
input_text = StringVar()
entry = Entry(root, textvariable=input_text, font=("Helvetica", 12), width=50)
entry.pack(pady=10)
entry.focus()

# create a Label to display results
result_label = Label(root, text="", font=("Helvetica", 12), bg='lightblue')
result_label.pack(pady=10)

# create Timer variable
start_time = None

# create Function to start timing and reset fields
def start_test(event):
    global start_time
    input_text.set("")  # Clear previous input
    result_label.config(text="")
    start_time = time.time()

# create Function to calculate typing speed and accuracy
def calculate_results():
    global start_time
    end_time = time.time()
    input_string = input_text.get()
    length_of_input = len(input_string.split())
    correct_words = len(set(input_string.split()) & set(test_string.split()))
    accuracy = (correct_words / word_count) * 100
    time_taken = end_time - start_time
    words_per_minute = (length_of_input / time_taken) * 60 if time_taken > 0 else 0

    # create to Display results
    result_text = (
        f"Total words: {length_of_input}\n"
        f"Time used: {round(time_taken, 2)} seconds\n"
        f"Accuracy: {round(accuracy, 2)}%\n"
        f"Speed: {round(words_per_minute, 2)} WPM"
    )
    result_label.config(text=result_text)

# create Button to start the test
start_button = Button(root, text="Start Test", command=lambda: start_test(None), font=("Helvetica", 12), bg='green', fg='white')
start_button.pack(pady=5)


root.bind('<Return>', start_test)

# create Button to calculate results after typing
calculate_button = Button(root, text="Submit", command=calculate_results, font=("Helvetica", 12), bg='blue', fg='white')
calculate_button.pack(pady=5)

# create Exit button
exit_button = Button(root, text="Exit", command=root.destroy, font=("Helvetica", 12), bg='red', fg='white')
exit_button.pack(pady=10)

# Main event loop to keep the window running
root.mainloop()
