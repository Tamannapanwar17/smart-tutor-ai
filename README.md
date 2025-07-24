mkdir smart-tutor-ai
cd smart-tutor-ai
   # app.py
   
   import streamlit as st
   import requests
   
   st.set_page_config(page_title="LearnLoop - AI Tutor", layout="wide")
   
   st.title("📚 LearnLoop - Offline AI Tutor")
   st.markdown("Ask your question and get a smart answer from a local AI model (Mistral via Ollama).")
   
   # Input box for question
   user_input = st.text_input("✏️ Enter your question:")
   
   # On submit
   if st.button("🧠 Ask AI"):
       if user_input.strip() == "":
           st.warning("Please enter a question.")
       else:
           try:
               response = requests.post("http://localhost:8000/ask", json={"question": user_input})
               if response.status_code == 200:
                   st.success("AI Response:")
                   st.write(response.json()["answer"])
               else:
                   st.error("Failed to get a response from the AI backend.")
           except Exception as e:
               st.error(f"❌ Error: {e}")
   streamlit run app.py
