Dyslexica: AI-Powered Text Enhancer for Dyslexics

Dyslexica is a Python-based tool designed to help individuals with dyslexia or anyone who wants to quickly correct grammar, spelling, and punctuation in their text. It leverages an AI model via the ollama library and automates the process with clipboard and keyboard interactions.
Features

    AI-powered grammar, spelling, and punctuation correction.
    Automatic text replacement in any application with minimal user interaction.
    Customizable hotkey for seamless integration.

How It Works

    Highlight the text you want to correct in any application.
    Press Alt+1 to copy the text, send it to the AI model, and replace it with the corrected version.

Requirements
System Requirements

    Python 3.7 or higher
    A supported operating system for ollama (macOS, Windows, or Linux)
    Internet connection for downloading the model

Python Libraries

    pyperclip
    pyautogui
    pynput
    ollama

Setup Instructions
Step 1: Clone the Repository

git clone https://github.com/electro-sheep/Dyslexica.git
cd dyslexica

Step 2: Install Dependencies

Install Python dependencies using:

pip install -r requirements.txt

Step 3: Install Ollama

    Follow the Ollama installation guide to install ollama on your system.
    After installation, verify that ollama is installed by running:

    ollama --version

Step 4: Download the Required Model

Dyslexica uses the gemma:2b-instruct model. Download it by running:

ollama pull gemma:2b-instruct

Running the Script

    Launch the script:

    python dyslexica.py

    Highlight any text in any application.
    Press Alt+1 to process the highlighted text, correct it, and replace it with the enhanced version.

Customization
Changing the Hotkey

Modify the '<alt>+1' mapping in the dyslexica.py script:

with keyboard.GlobalHotKeys({'<alt>+1': on_key_combination}) as listener:

Using a Different Model

Update the model name in the script:

response: ChatResponse = chat(model='your-model-name', messages=[ ... ])

