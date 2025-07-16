# Personal Desktop Assistance (Gen)

A Python-based virtual assistant with a GUI, speech-to-text, and text-to-speech capabilities. This assistant helps users interact with their desktop using voice commands and visual guidance.

## Features

- **Graphical User Interface:** User-friendly GUI for easy interaction.
- **Speech Recognition:** Converts spoken words to text.
- **Text to Speech:** Converts text responses to audible speech.
- **Weather Updates:** Get real-time weather information.
- **Action Automation:** Perform various desktop actions using voice or text commands.
- **Visual Identity:** Includes a robot assistant image for a friendly interface.

## Directory Structure

```
personal-desktop-assistance/
│
├── __pycache__/                # Compiled Python files
├── GUI.py                      # Main GUI implementation
├── action.py                   # Handles various desktop actions
├── speech_to_text.py           # Speech recognition logic
├── text_to_speech.py           # Text-to-speech functionality
├── weather.py                  # Weather info retrieval
└── image/
    └── cute-smiling-robot-virtual-assistant-in-yo  # Robot assistant image
```

## Requirements

- Python 3.x
- PyQt5 or Tkinter (for GUI)
- SpeechRecognition
- pyttsx3 or gTTS
- Requests (for weather API)
- Pillow (if working with images)

*Install requirements with:*
```bash
pip install -r requirements.txt
```
*(Create a `requirements.txt` if not present.)*

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Payel-19/personal-desktop-assistance.git
   cd personal-desktop-assistance/personal-desktop-assistance
   ```
2. Run the assistant:
   ```bash
   python GUI.py
   ```
3. Use the GUI to interact with your virtual assistant.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](../LICENSE)

---

Feel free to edit this README to match any additional features or specifics of your project. If you want a more detailed or custom README, let me know!
