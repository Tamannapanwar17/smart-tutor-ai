import streamlit as st
import requests
import pyttsx3
import speech_recognition as sr
from fpdf import FPDF

# Text-to-speech setup
engine = pyttsx3.init()

# Streamlit UI setup
st.set_page_config(page_title="🧠 LearnLoop AI Tutor", layout="centered")
st.title("📚 LearnLoop – Local AI Tutor")
st.markdown("Ask a question and get an answer from LLaMA2 running locally!")

# Voice input toggle
use_voice = st.toggle("🎙️ Use voice input")

# Input handling
question = ""

if use_voice:
    if st.button("🎤 Record your voice"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎧 Listening... Speak now.")
            audio = recognizer.listen(source)

        try:
            question = recognizer.recognize_google(audio)
            st.success(f"📝 Recognized: {question}")
        except sr.UnknownValueError:
            st.error("❌ Could not understand audio.")
        except sr.RequestError:
            st.error("❌ Speech recognition service unavailable.")
else:
    question = st.text_input("📝 Enter your question", placeholder="e.g., What is the law of conservation of mass?")

# Answer box placeholder
answer = ""

if question:
    with st.spinner("💬 Thinking..."):
        payload = {
            "model": "llama2",
            "prompt": question,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 100
            }
        }

        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=120)
            answer = response.json().get('response', 'No response received.')
            st.success("✅ Answer:")
            st.write(answer)

        except requests.exceptions.Timeout:
            st.error("⏱️ Timeout! The model took too long to respond.")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Export options
col1, col2, col3 = st.columns(3)

with col1:
    if answer and st.button("📤 Export as TXT"):
        with open("answer.txt", "w", encoding="utf-8") as f:
            f.write(answer)
        st.success("✅ Exported to `answer.txt`")

with col2:
    if answer and st.button("📄 Export as PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, answer)
        pdf.output("answer.pdf")
        st.success("✅ Exported to `answer.pdf`")

with col3:
    if answer and st.button("🔊 Speak Answer"):
        engine.say(answer)
        engine.runAndWait()
