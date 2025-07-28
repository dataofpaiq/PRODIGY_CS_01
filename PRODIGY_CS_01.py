'''
Task #1
Create a oython program that can encrypt and 
decrypt text using the caesar chipper algorithm.
'''

import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Encryption
def Encryption(message, shift):
    result = ""
    for char in message:
        if char == " ":
            result += " "
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Caesar Cipher Decryption
def Decryption(message, shift):
    return Encryption(message, -shift)

# Encrypt action
def encrypt_message():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
        encrypted = Encryption(message, shift)
        entry_output.delete(0, tk.END)
        entry_output.insert(0, encrypted)
    except ValueError:
        messagebox.showerror("Invalid input", "Shift value must be an integer.")

# Decrypt action
def decrypt_message():
    message = entry_message.get()
    try:
        shift = int(entry_shift.get())
        decrypted = Decryption(message, shift)
        entry_output.delete(0, tk.END)
        entry_output.insert(0, decrypted)
    except ValueError:
        messagebox.showerror("Invalid input", "Shift value must be an integer.")

# GUI Setup
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x280")

# Input message
tk.Label(window, text="Enter Message:").pack(pady=5)
entry_message = tk.Entry(window, width=50)
entry_message.pack()

# Input shift value
tk.Label(window, text="Enter Shift Value:").pack(pady=5)
entry_shift = tk.Entry(window, width=10)
entry_shift.pack()

# Encrypt and Decrypt buttons
tk.Button(window, text="Encrypt", command=encrypt_message).pack(pady=5)
tk.Button(window, text="Decrypt", command=decrypt_message).pack(pady=5)

# Output box
tk.Label(window, text="Output:").pack(pady=5)
entry_output = tk.Entry(window, width=50)
entry_output.pack()

# Start GUI loop
window.mainloop()
