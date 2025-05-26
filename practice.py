import whisper

model = whisper.load_model("tiny")
result = model.transcribe("sample.mp3")
print(result["text"])