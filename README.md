# Auto Type Writer

A simple Python tool that automatically types your text anywhere after a short countdown. Perfect for demos, repetitive typing tasks, or fun automation.

## Features
- Large multi-line input box for easy text entry
- Countdown popup (5 seconds) before typing
- Fast automated typing
- Automatically exits after typing finishes
- Minimal dependencies

## Requirements
- Python 3.8 or higher
- [pyautogui](https://pypi.org/project/PyAutoGUI/) (`pip install pyautogui`)
- Tkinter (built-in with Python)

> **Note for macOS users:** You may need to allow accessibility permissions in `System Preferences → Security & Privacy → Accessibility` to let `pyautogui` control your computer.

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/phanee27/AutoTypeWriterTool
   
2. **Navigate into the project folder**  
   ```bash
   cd AutoTypeWriterTool

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

  
4. **Run the tool**
   ```bash
   python AutoTypeWriter.py
