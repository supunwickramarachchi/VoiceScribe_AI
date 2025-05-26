import customtkinter as ctk
import whisper
import speech_recognition as sr
from datetime import datetime
from tkinter import filedialog
from pathlib import Path
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Voice Note Taker")
app.geometry("600x400")

model = whisper.load_model("base")

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        file_name = Path(file_path).name
        file_name_label.configure(text=f"Selected File: {file_name}")
    
def transcribe_file():
    
    path = file_path
    result = model.transcribe(path)
    text_box.delete
    text_box.delete("1.0", "end")
    text_box.insert("1.0", result["text"])
    save_text(result["text"])
    
def save_text(text):
    if not os.path.exists("notes"):
        os.mkdir("notes")
    filename = f"notes/note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    status_label.configure(text=f"Saved: {filename}")
    
    
def copy_transcribe_text():
    text = text_box.get("1.0", "end")
    app.clipboard_clear()
    app.clipboard_append(text)
    app.update()
    
file_path = ctk.CTkButton(app, text="Select the File", command=select_file)
file_path.pack(pady=10)

file_name_label= ctk.CTkLabel(app, text="No file selected")
file_name_label.pack(pady=5)

transcribe_btn = ctk.CTkButton(app, text="Transcribe File", command=transcribe_file)
transcribe_btn.pack(pady=5)

mic_btn = ctk.CTkButton(app, text="Record from Microphone", command=None)
mic_btn.pack(pady=5)

text_box = ctk.CTkTextbox(app, width=500, height=150)
text_box.pack(pady=10)

status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=5)

copy_button = ctk.CTkButton(app, text="Copy Text", command=copy_transcribe_text)
copy_button.pack()

app.mainloop()
