import os
import shutil
import logging
import tkinter as tk
from tkinter import filedialog, messagebox

logging.basicConfig(filename="file_organizer.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

FILE_CATEGORIES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar"]
}

def organize_files(directory):
    # if not os.path.exists(directory):
    #     messagebox.showerror("Error", "Invalid Directory")
    #     return
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category_folder = os.path.join(directory, category)
                    
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    
                    try:
                        shutil.move(file_path, os.path.join(category_folder, file))
                        logging.info(f"Moved: {file} -> {category}/")
                    except Exception as e:
                        logging.error(f"Error moving {file}: {e}")
    
    messagebox.showinfo("Success", "Files organized successfully!")

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)

box = tk.Tk()
box.title("File Organizer")
box.geometry("300x150")

tk.Label(box, text="Select a folder to organize", font=("Arial", 12)).pack(pady=10)
tk.Button(box, text="Choose Folder", command=select_folder).pack(pady=10)
tk.Button(box, text="Exit", command=box.quit).pack(pady=10)

box.mainloop()
