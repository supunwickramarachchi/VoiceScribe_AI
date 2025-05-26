# Voice Note Transcriber & Summarizer

This is a Python-based desktop application that allows users to transcribe speech from audio files or a microphone, and then summarize the transcript using AI. It features a modern GUI built with `customtkinter`, and integrates with OpenAI's GPT model for intelligent summarization.

## Features

- 🎙️ Transcribe speech from `.mp3` files or live microphone input using OpenAI's Whisper
- 🧠 Summarize transcriptions using OpenAI GPT-4
- 🖥️ Simple and modern GUI using `customtkinter`
- 🌗 Toggle between Light and Dark mode
- 💾 Auto-save transcriptions and summaries to a folder
- 🔧 Easy-to-extend architecture for future features

---

## Why I Built This

I developed this project to:

- Practice real-world software engineering using Python
- Learn to integrate advanced AI models like Whisper and GPT into desktop applications
- Understand GUI programming with `customtkinter`
- Explore audio processing and natural language understanding

This project was created from scratch and built step-by-step to demonstrate my growing skill set in software engineering, AI integration, and user-centered design.

---

## How This Solves Real-World Problems

- **Note-Taking for Lectures & Meetings**: Automatically transcribes and summarizes spoken content, making it easier to review and recall key points.
- **Accessibility Tool**: Helps individuals with hearing impairments or attention disorders by providing clean summaries of audio content.
- **Productivity Booster**: Saves time by reducing the need to manually take notes or extract summaries from long recordings.
- **Educational Aid**: Students, teachers, and researchers can use it to process and understand spoken information more effectively.

---

## Technologies Used

| Technology       | Purpose                                |
|------------------|----------------------------------------|
| Python           | Main programming language              |
| OpenAI Whisper   | Audio transcription (speech-to-text)   |
| OpenAI GPT-4     | Text summarization                     |
| customtkinter    | GUI framework                          |
| pyaudio / sounddevice | Microphone input support         |
| ffmpeg           | Required for Whisper audio preprocessing |

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/voice-note-transcriber.git
cd voice-note-transcriber
```
### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. Download & Setup ffmpeg
_** Make sure ffmpeg is installed and added to your system PATH: **_
- Download ffmpeg

- Extract to C:\ffmpeg

- Add C:\ffmpeg\bin to your system environment variables → PATH

### 5. Add Your OpenAI API Key
**_Create a .env file or modify the script to include:_**
```bash
import openai
openai.api_key = "your_api_key_here"
```
### 6. Run the App
```bash
python app.py
```
## Future Improvements
- Export to PDF or Word

- Add language selection

- Speaker diarization (who said what)

- Better error handling and notifications

- Multilingual transcription and summarization

- Convert to a Windows executable (.exe) using pyinstaller

## What I Learned
- This project helped me gain experience in:

- Full-stack desktop software development using Python

- Audio processing with ffmpeg and Whisper

- AI integration (speech-to-text and text summarization)

- GUI development and user experience design

- Working with real-world APIs (OpenAI)

- Handling files, user input, and system interaction

- Version control with Git and publishing on GitHub

## Author
Supun Wickramarachchi
Aspiring Software & Space Engineer | Python Developer | AI Enthusiast
GitHub Profile
LinkedIn Profile (optional)

_#Python #OpenAI #Whisper #SpeechToText #Summarization #AI #AudioProcessing 
#DesktopApp #TranscriptionTool #CustomTkinter #SoftwareEngineering #GitHubProjects 
#AIProductivity #VoiceToText #TextSummarizer #RealWorldProjects #FFmpeg_
