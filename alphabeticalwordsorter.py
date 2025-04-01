import tkinter as tk
from tkinter import font

def sort_words():
    # Get input text and split it into words
    words = entry.get()
    words_list = words.split()
    
    # Sort words in a case-insensitive manner
    sorted_list = sorted(words_list, key=lambda word: word.lower())
    
    # Display the sorted words
    result_var.set(" ".join(sorted_list))

# Create the main window
root = tk.Tk()
root.title("Colorful Alphabetical Word Sorter")
root.geometry("500x300")
root.configure(bg="#FFD700")  # Gold background

# Custom fonts
title_font = font.Font(family="Helvetica", size=20, weight="bold")
label_font = font.Font(family="Helvetica", size=14, weight="bold")
entry_font = font.Font(family="Helvetica", size=12)

# Title label
title_label = tk.Label(root, text="Alphabetical Word Sorter", bg="#FFD700", fg="#8B0000", font=title_font)
title_label.pack(pady=10)

# Instruction label
instruction_label = tk.Label(root, text="Enter words separated by spaces:", bg="#FFD700", fg="#00008B", font=label_font)
instruction_label.pack(pady=5)

# Entry widget for user input
entry = tk.Entry(root, width=50, font=entry_font, bg="#FFFFFF", fg="#000000", relief=tk.RIDGE, bd=2)
entry.pack(pady=10)

# Button to sort words
sort_button = tk.Button(root, text="Sort Words", command=sort_words, font=label_font, bg="#32CD32", fg="#FFFFFF", activebackground="#228B22", relief=tk.RAISED, bd=3)
sort_button.pack(pady=10)

# Label to display the sorted result
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, bg="#FFD700", fg="#00008B", font=label_font)
result_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()