import time
import google.generativeai as genai
import pyperclip
import pyautogui

# Configure the Gemini API client
genai.configure(api_key="[YOUR API KEY HERE]")


def send_to_gemini(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            'Analyse the question and generate error free codes including any updated api codes if available with no comments or junk code, with all required optimizations (give only the codes, no junk data) : ' + str(
                prompt)
        )
        return response.text
    except Exception as e:
        print(f"Error in sending message: {e}")
        return None


def write_to_file(filename, data):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(data + "\n")
        print(f"Data written to {filename} successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    previous_clipboard_content = pyperclip.paste()

    while True:
        current_clipboard_content = pyperclip.paste()

        if current_clipboard_content != previous_clipboard_content:
            print(f"Clipboard changed: {current_clipboard_content}")

            response = send_to_gemini(current_clipboard_content)

            if response:
                print(f"Gemini Response: {response}")

                if str(response).startswith("```"):
                    lines = response.splitlines()
                    response = "\n".join(lines[1:-1]) if len(lines) > 2 else ""
                pyautogui.typewrite(response, interval=0.02)

                write_to_file("Genr8.log", "\n\nQuestion:\n" + current_clipboard_content + "\n\nAnswer:\n" + response)

            previous_clipboard_content = current_clipboard_content

        time.sleep(1)


if __name__ == "__main__":
    main()
