# Genr8

![Genr8 Logo](https://via.placeholder.com/800x200.png?text=Genr8+-+AI+Code+Generator)

## 🚀 Overview
**Genr8** is a powerful clipboard monitoring tool that leverages Google's **Gemini AI** to generate optimized, error-free code snippets on the fly. Whenever you copy a programming-related question, Genr8 automatically fetches the best possible code response and types it out for you instantly!

## ✨ Features
- **Real-time Clipboard Monitoring**: Detects changes in clipboard content.
- **AI-Powered Code Generation**: Uses Gemini AI to generate accurate and updated code.
- **Auto Typing**: Automatically types out the generated code.
- **Optimized Code Responses**: Ensures no junk or unnecessary comments in the output.
- **Logging System**: Saves all questions and answers for future reference.

## 🔧 Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/genr8.git
   cd genr8
   ```
2. Install dependencies:
   ```sh
   pip install google-generativeai pyperclip pyautogui
   ```
3. Set up the Gemini API key:
   - Replace `api_key="YOUR_GEMINI_API_KEY"` inside the script.

## 🏃‍♂️ Usage

1. Run the script:
   ```sh
   python genr8.py
   ```
2. Copy any programming-related question.
3. Watch as Genr8 processes the question, generates code, and types it out instantly!

## 📂 Log File
All processed questions and answers are stored in `Genr8.log`, formatted as:
```
Question:
<Your copied question>

Answer:
<Generated AI Response>
```

## ⚠️ Disclaimer
- Ensure you comply with Google Gemini's API usage policies.
- Use responsibly, and verify generated code before execution.

## 🛠 Future Enhancements
- Support for multiple programming languages.
- Configurable typing speed and response format.
- GUI-based interface for better usability.

## 🎯 Contributing
Pull requests are welcome! If you’d like to contribute, please fork the repository and create a new branch for your changes.

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

🎉 **Happy Coding with Genr8!** 🚀
