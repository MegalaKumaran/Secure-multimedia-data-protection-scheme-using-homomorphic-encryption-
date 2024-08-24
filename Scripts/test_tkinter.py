import tkinter as tk
from tkinter import messagebox
import subprocess

def execute_scripts():
    try:
        # Call imageToMatrix.py
        subprocess.run(["python", "imageToMatrix.py"])
        # Call featureExtraction.py
        subprocess.run(["python", "featureExtraction.py"])
        # Call encryption.py
        subprocess.run(["python", "encryption.py"])
        # Call encryptImage.py
        subprocess.run(["python", "encryptImage.py"])
        # Call decryptImage.py
        subprocess.run(["python", "decryptImage.py"])
        # Call decryption.py
        subprocess.run(["python", "decryption.py"])
        # Call matrixToImage.py
        subprocess.run(["python", "matrixToImage.py"])
        messagebox.showinfo("Execution", "Scripts executed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Script Executor")

execute_button = tk.Button(root, text="Execute Scripts", command=execute_scripts)
execute_button.pack()

root.mainloop()
