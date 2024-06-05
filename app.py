import streamlit as st
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *

# Initialize floating features for the interface
float_init()

# Initialize session state for managing chat messages
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I assist you today?"}]

initialize_session_state()

st.title("OpenAI Conversational Chatbot 🤖")

footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()
