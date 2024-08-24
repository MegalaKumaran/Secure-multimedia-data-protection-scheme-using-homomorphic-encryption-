import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import time
from PIL import ImageTk, Image

# Outside any function
selected_data = {}  # Dictionary to store selected data

def choose_image():
    global selected_data
    selected_file = filedialog.askopenfilename()
    if selected_file:
        start_encryption_button.config(state=tk.NORMAL)
        selected_data["image"] = selected_file  # Update dictionary with image path
        img = Image.open(selected_file)
        image_width, image_height = img.size
        #img.thumbnail((300, 300))  # Resize the image to fit in the window
        
        # Convert the image to a format that Tkinter can display
        tk_image = ImageTk.PhotoImage(img)
        
        # Create a canvas to display the image
        canvas.delete("all")  # Clear any existing image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        canvas.image = tk_image

def choose_text():
    global selected_data
    text = text_entry.get("1.0", "end-1c")
    if text:
        start_encryption_button.config(state=tk.NORMAL)
        selected_data["text"] = text  # Update dictionary with text data

def choose_realtime_data():
    global selected_data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        start_encryption_button.config(state=tk.NORMAL)
        selected_data["realtime"] = file_path  # Update dictionary with real-time data path

def execute_encryption_scripts():
    try:
        
        if "image" in selected_data:
            # Call image encryption scripts with selected_data["image"]
            subprocess.run(["python", "imageToMatrix.py", selected_data["image"]])
            # Call featureExtraction.py
            subprocess.run(["python", "featureExtraction.py", selected_data["image"]])
            # Call encryption.py
            start_time=time.time()
            subprocess.run(["python", "imageEncryption.py"])
            end_time=time.time()
            # Call encryptImage.py
            subprocess.run(["python", "encryptImage.py"])
            encrypted_image=Image.open("encrypted_image.png") # Update dictionary with image path
            tk_image = ImageTk.PhotoImage(encrypted_image)
            canvas2.delete("all")  # Clear any existing image on the canvas
            canvas2.create_image(0, 0, anchor=tk.NW, image=tk_image)
            canvas2.image = tk_image
            messagebox.showinfo("Execution", "Encryption completed successfully.")
            
            start_decryption_button.config(state=tk.NORMAL)  # Enable decryption button after encryption
            
            
        elif "text" in selected_data:
            start_time=time.time()
            # Call text encryption scripts with selected_data["text"]
            subprocess.run(["python", "textEncryption.py", selected_data["text"]])
            end_time=time.time()
            messagebox.showinfo("Execution", "Text Encryption completed successfully.")
            def read_file(filename):
                with open(filename) as file:
                    text=file.read()
                return text
            def load_text_to_textbox(textbox,filename):
                text=read_file(filename)
                text_entry.delete("1.0","end")
                text_entry.insert("1.0",text)
            #text_entry = tk.Text(root, wrap="word")
            #text_entry.pack(expand=False, fill="both")
            filename = "ciphertext.txt"
            load_text_to_textbox(text_entry, filename)
            start_decryption_button.config(state=tk.NORMAL)  # Enable decryption button after encryption
            
        elif "realtime" in selected_data:
            start_time=time.time()
            # Call real-time data encryption scripts with selected_data["realtime"]
            subprocess.run(["python", "key.py", selected_data["realtime"]])
            subprocess.run(["python", "RealTimeEncryption.py", selected_data["realtime"]])
            end_time=time.time()
            messagebox.showinfo("Execution", "Real-time Data Encryption completed successfully.")
            start_decryption_button.config(state=tk.NORMAL)  # Enable decryption button after encryption
           

        elif not any(selected_data):
            messagebox.showerror("Error", "No data selected for encryption.")

        else:
            selected_data.clear()
            start_decryption_button.config(state=tk.NORMAL)
        encryption_duration=end_time-start_time
        messagebox.showinfo("Execution Time", f"Encryption completed in {encryption_duration:.2f} seconds.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encryption: {e}")

def execute_decryption_scripts():
    try:
        if "image" in selected_data:
            # Call image decryption scripts
            
            subprocess.run(["python", "decryptImage.py"])
            start_timer=time.time()
            subprocess.run(["python", "imageDecryption.py"])
            end_timer=time.time()
            subprocess.run(["python", "matrixToImage.py"])
            messagebox.showinfo("Execution", "Image Decryption completed successfully.")
            decrypted_image=Image.open("restored_image.png") # Update dictionary with image path
            tk_image = ImageTk.PhotoImage(decrypted_image)
            canvas3.delete("all")  # Clear any existing image on the canvas
            canvas3.create_image(0, 0, anchor=tk.NW, image=tk_image)
            canvas3.image = tk_image
           
        elif "text" in selected_data:
            start_timer=time.time()
            # Call text decryption scripts with selected_data["text"] (assuming decryption uses the original text)
            subprocess.run(["python", "textDecryption.py", selected_data["text"]])
            end_timer=time.time()
            messagebox.showinfo("Execution", "Text Decryption completed successfully.")
            def read_file(filename):
                with open(filename) as file:
                    text=file.read()
                return text
            def load_text_to_textbox(textbox,filename):
                text=read_file(filename)
                text_entry.delete("1.0","end")
                text_entry.insert("1.0",text)
            #text_entry = tk.Text(root, wrap="word")
            #text_entry.pack(expand=False, fill="both")
            filename = "decryptedText.txt"
            load_text_to_textbox(text_entry, filename)
        elif "realtime" in selected_data:
            start_timer=time.time()
            # Call real-time data decryption scripts
            subprocess.run(["python", "realTimeDecryption.py"])
            end_timer=time.time()
            subprocess.run(["python", "check.py"])
            messagebox.showinfo("Execution", "Real-time Data Decryption completed successfully.")
        if not any(selected_data):
            messagebox.showerror("Error", "No data selected for decryption.")
        else:
            selected_data.clear()
        decryption_duration=end_timer-start_timer
        messagebox.showinfo("Execution Time", f"Decryption completed in {decryption_duration:.2f} seconds.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decryption: {e}")
    
def center_window(root):
    width = root.winfo_screenwidth() 
    height = root.winfo_screenheight()
    x = (root.winfo_screenwidth() - width) / 2
    y = (root.winfo_screenheight() - height) / 2
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

def center_window_after_delay(root, event):
    root.after(200, center_window, root)  # Adjust the delay time as needed

root = tk.Tk()
root.title("Script Executor")
center_window(root)  # Center the window initially
root.configure(bg='#f0f0f0')  # Set background color

bg_image = Image.open("bg.jpg")
bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
background_label = tk.Label(root, image=bg_photo)
background_label.image = bg_photo
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add labels for better context

heading1_label = tk.Label(root, text="SECURE MEDICAL DATA ENCRYPTION", bg='#f0f0f0', font=('Helvetica', 14))
heading1_label.place(x=550,y=25)

heading2_label= tk.Label(root, text="  USING HOMOMORPHIC TECHNIQUES " , bg='#f0f0f0', font=('Helvetica', 14))
heading2_label.place(x=550,y=50)

choose_option_label = tk.Label(root, text="Select Encryption Option:", bg='#f0f0f0', font=('Helvetica', 14))
choose_option_label.place(x=650,y=100)

# Option buttons for encryption type selection
option_image_button = tk.Button(root, text="Encrypt Image", command=choose_image, bg='#4CAF50', fg='black', font=('Helvetica', 12))
option_image_button.place(x=510,y=150)

option_realtime_button = tk.Button(root, text="Encrypt Real-time Data", command=choose_realtime_data, bg='#4CAF50', fg='black', font=('Helvetica', 12))
option_realtime_button.place(x=650,y=150)
#option_realtime_button.pack(pady=10,padx=650,anchor='w')

option_text_button = tk.Button(root, text="Encrypt Text", command=choose_text, bg='#4CAF50', fg='black', font=('Helvetica', 12))
option_text_button.place(x=850,y=150)

# Entry field for entering text
text_entry = tk.Text(root, height=4, width=40, font=('Helvetica', 12))
text_entry.place(x=550,y=200)


# Add buttons for encryption execution
start_encryption_button = tk.Button(root, text="Start Encryption", command=execute_encryption_scripts, state=tk.DISABLED, bg='#D0E9FF', fg='black', font=('Helvetica', 12))
start_encryption_button.place(x=650,y=300)

start_decryption_button = tk.Button(root, text="Start Decryption", command=execute_decryption_scripts, state=tk.DISABLED, bg='#D0E9FF', fg='black', font=('Helvetica', 12))
start_decryption_button.place(x=650,y=350)

original_image_label = tk.Label(root, text="Original Image:", bg='lightblue', font=('Helvetica', 14))
original_image_label.place(x=100,y=400)

encrypted_image_label = tk.Label(root, text="Encrypted Image:", bg='lightblue', font=('Helvetica', 14))
encrypted_image_label.place(x=600,y=400)

restored_image_label = tk.Label(root, text="Restored Image:", bg='lightblue', font=('Helvetica', 14))
restored_image_label.place(x=1100,y=400)

# Create a canvas to display the image

canvas = tk.Canvas(root, width= 300, height=300, bg='lightblue')
canvas.place(x=100,y=430)

canvas2 = tk.Canvas(root, width= 300, height=300, bg='lightblue')
canvas2.place(x=600,y=430)

canvas3 = tk.Canvas(root, width= 300, height=300, bg='lightblue')
canvas3.place(x=1100,y=430)

# Create canvas4
canvas4 = tk.Canvas(root, width=480, height=126, bg='lightgreen')
# Place canvas4 at the calculated coordinates
canvas4.place(x=1050, y=0)
logo_image=Image.open("SASTRA.jpg") # Update dictionary with image path
tk_image = ImageTk.PhotoImage(logo_image)
canvas4.delete("all")  # Clear any existing image on the canvas
canvas4.create_image(0, 0, anchor=tk.NW, image=tk_image)
canvas4.image = tk_image

canvas5 = tk.Canvas(root, width=480, height=126, bg='lightgreen')
# Place canvas4 at the calculated coordinates
canvas5.place(x=0, y=0)
logo_image=Image.open("SASTRA.jpg") # Update dictionary with image path
tk_image = ImageTk.PhotoImage(logo_image)
canvas5.delete("all")  # Clear any existing image on the canvas
canvas5.create_image(0, 0, anchor=tk.NW, image=tk_image)
canvas5.image = tk_image


#canvas4.pack(side=tk.BOTTOM ,padx=0,pady=80)

    
# Bind the center_window_after_delay function to the window configure event
root.bind("<Configure>", lambda event: center_window_after_delay(root, event))

root.mainloop()