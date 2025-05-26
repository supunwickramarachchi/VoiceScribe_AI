import whisper
import os
from datetime import datetime

model = whisper.load_model("base")

file_path = input("Enter the path to your audio file (sample.mp3): ")

print("Transcribing...")
result = model.transcribe(file_path)

text = result['text']
print("\n--- Transcription ---\n")
print(text)

if not os.path.exists("notes"):
    os.mkdir("notes")
    
filename = f"notes/note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(text)
    
print(f"\n✅ Transcription saved to {filename}")