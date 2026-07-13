# Classical Substitution Cipher (Caesar Cipher)
print("# ---------------- T120 DHEERAJ SINGH ---------------- #")
print("Classical Substitution Cipher (Caesar Cipher))")
print()
def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(cipher_text, shift):
    result = ""

    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char

    return result

text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted = encrypt(text, shift)
print("Encrypted Message:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted Message:", decrypted)




















# ---------------- GUI ---------------- #

import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def encrypt_text():
    try:
        text = txt_message.get()
        shift = int(txt_shift.get())

        encrypted = caesar_encrypt(text, shift)

        result_box.config(state="normal")
        result_box.delete(0, tk.END)
        result_box.insert(0, encrypted)
        result_box.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid shift value.")


def decrypt_text():
    try:
        text = txt_message.get()
        shift = int(txt_shift.get())

        decrypted = caesar_decrypt(text, shift)

        result_box.config(state="normal")
        result_box.delete(0, tk.END)
        result_box.insert(0, decrypted)
        result_box.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid shift value.")

def clear_all():
    txt_message.delete(0, tk.END)
    txt_shift.delete(0, tk.END)

    result_box.config(state="normal")
    result_box.delete(0, tk.END)
    result_box.config(state="readonly")

root = tk.Tk()
root.title("# ---------------- T120 DHEERAJ SINGH ---------------- #")
root.geometry("500x320")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Classical Substitution Cipher (Caesar Cipher)",
    font=("Arial", 15, "bold")
)
title.pack(pady=15)

tk.Label(root, text="Enter Message:", font=("Arial", 11)).pack()

txt_message = tk.Entry(root, width=50, font=("Arial", 11))
txt_message.pack(pady=5)

tk.Label(root, text="Shift Value:", font=("Arial", 11)).pack()

txt_shift = tk.Entry(root, width=10, font=("Arial", 11))
txt_shift.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=15)

btn_encrypt = tk.Button(
    frame,
    text="Encrypt",
    width=12,
    bg="lightgreen",
    command=encrypt_text
)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(
    frame,
    text="Decrypt",
    width=12,
    bg="lightblue",
    command=decrypt_text
)
btn_decrypt.grid(row=0, column=1, padx=10)

btn_clear = tk.Button(
    frame,
    text="Clear",
    width=12,
    bg="tomato",
    command=clear_all
)
btn_clear.grid(row=0, column=2, padx=10)

tk.Label(root, text="Result:", font=("Arial", 11, "bold")).pack()

result_box = tk.Entry(root, width=50, font=("Arial", 11), state="readonly")
result_box.pack(pady=5)

root.mainloop()
