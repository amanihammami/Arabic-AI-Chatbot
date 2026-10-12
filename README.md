# 🤖 Arabic AI Chatbot

A simple, interactive custom AI Chatbot web application powered by **Streamlit** and the **OpenAI API**.

## 🚀 Features
* **Streaming Responses:** Live token-by-token message text generation.
* **Session Memory:** Keeps track of conversation history during your chat session.
* **Secure Key Management:** Utilizes environment variables to keep API keys hidden and safe.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Arabic-AI-Chatbot
   ```

2. **Install the required packages:**
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Configure your API Key:**
   * Create a file named `.env` in the root folder.
   * Add your private OpenAI API Key inside it:
     ```text
     OPENAI_API_KEY=your_actual_api_key_here
     ```

4. **Run the application:**
   ```bash
   python -m streamlit run chatbot1.py
   ```

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
