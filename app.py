import streamlit as st
from streamlit_mic_recorder import speech_to_text
from chatbot import ChatBot
from tts import TTS
import asyncio
st.title("🎙️Talk with Mahendra Kumar Reddy")

# Speech-to-Text

text = speech_to_text(language='en', use_container_width=True, just_once=True, key='STT',start_prompt="Ask question",stop_prompt="Generate response")

chatbot=ChatBot()
tts=TTS()
if text:
    st.write(f"**You said:** {text}")
    response = chatbot.get_response(text)
    outfile = asyncio.run(tts.text_to_audio(response))
    st.audio(outfile,autoplay=True)
    st.write(f"**Mahi:** {response}")



