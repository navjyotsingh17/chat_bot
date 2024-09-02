import pyautogui
import time
import pyperclip
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

def check_last_message_sender(chat_history, sender_name="Namo"):
    # Get the messages
    messages = chat_history.split("/2024]")[-1]

    if sender_name in messages:
        return True
    else:
        False    

# Click on the application located at (852, 1050)
pyautogui.click(852, 1050)

while True:
    # Wait for 2 seconds before starting (so you can switch to the desired screen)
    time.sleep(2)

    # Wait for the application to open (adjust the time if needed)
    time.sleep(3)

    # Move the mouse to the start position (453, 186) and drag to (492, 998)
    pyautogui.moveTo(697, 253)
    pyautogui.dragTo(1844, 897, duration=2, button='left')

    # Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1836, 834)

    # Give some time for the clipboard to process the copy action
    time.sleep(1)

    # Get the copied text from the clipboard
    chat_history = pyperclip.paste()

    # Print the copied text
    # print("Chat history:", chat_history)

    if check_last_message_sender(chat_history):

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named navjyot, and he speaks english and hindi languages. You are from India and you are a software developer engineer. Analyze the chat history and respond like navjyot"},
            {
                "role": "user",
                "content": chat_history
            }
        ]
        )

        response = completion.choices[0].message.content

        pyperclip.copy(response)

        # Give some time for the clipboard to process the copy action
        time.sleep(1)

        # Click on the target location at (1135, 960)
        pyautogui.click(1135, 960)

        # Paste the copied text
        pyautogui.hotkey('ctrl', 'v')

        # Press Enter
        pyautogui.press('enter')
