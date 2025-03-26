# 🎙️ AI Voice Chatbot

This is an AI-powered **Speech-to-Text & Voice Chatbot** built with **Streamlit**. It allows users to:
- Convert speech to text
- Get responses from an AI chatbot
- Convert AI responses to speech and play them at 1.25x speed

🚀 **Live Demo:** [Your Streamlit Link Here]

---

## 🛠️ Setup Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/ai-voice-chatbot.git
cd ai-voice-chatbot
```

### 2️⃣ Create & Activate Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a **.env** file in the project root and add:
```bash
GROQ_API_KEY=your_api_key_here
```
🔑 **Get Your API Key:** [Groq API Key](https://groq.com/api-keys)

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📜 Features
✅ Speech-to-Text (STT) using **streamlit_mic_recorder**  
✅ AI Chatbot powered by **Groq API**  
✅ Text-to-Speech (TTS) using **edge_tts**  
✅ Autoplay chatbot responses at **1.25x speed**  
✅ Streamlit UI with **Microphone & Wave Animation**  

---

## 📌 License
This project is **open-source** and free to use under the [MIT License](LICENSE). Feel free to contribute! 🚀

