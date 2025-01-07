import pyperclip
import pyautogui
from pynput import keyboard
from ollama import chat
from ollama import ChatResponse
import time

# Reduce pyautogui's default pause time
pyautogui.PAUSE = 0.1  # Default is 0.1 seconds; adjust for faster execution

def process_highlighted_text():
    try:
        # Step 1: Simulate "Ctrl+C" to copy the highlighted text to the clipboard
        print("[INFO] Copying highlighted text...")
        pyautogui.hotkey('ctrl', 'c')  # Simulate copy action
        time.sleep(0.5)  # Allow clipboard to update

        # Step 2: Capture the clipboard content
        text = pyperclip.paste().strip()
        if not text:
            print("[ERROR] No text found in clipboard. Ensure text is highlighted.")
            return

        # Step 3: Send the captured text to the AI model with the refined prompt
        print("[INFO] Sending text to the model...")
        prompt = (
            "Correct the following text by fixing only grammar, spelling, and punctuation mistakes. "
            "Enhance readability where necessary but do not change the original meaning. "
            "Preserve line breaks, formatting, and structure. "
            "Respond only with the corrected text, without quotation marks or additional formatting. \n\n"
            f"Text to correct: {text}"
        )
        response: ChatResponse = chat(model='gemma:2b-instruct', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])

        # Step 4: Process the AI response
        result = response.message.content.strip()
        if not result:
            print("[ERROR] No valid response received from the model.")
            return

        # Remove any enclosing quotation marks
        if result.startswith('"') and result.endswith('"'):
            result = result[1:-1]

        # Step 5: Update the clipboard and simulate "Ctrl+V"
        pyperclip.copy(result)
        print("[INFO] Text processed and clipboard updated.")
        pyautogui.hotkey('ctrl', 'v')  # Simulate paste action

    except Exception as e:
        print(f"[ERROR] An exception occurred: {e}")

def on_key_combination():
    """Triggered by Alt+1 hotkey."""
    process_highlighted_text()

def main():
    print("Press Alt+1 to send highlighted text to Ollama and replace it.")
    with keyboard.GlobalHotKeys({'<alt>+1': on_key_combination}) as listener:
        listener.join()

if __name__ == "__main__":
    main()
