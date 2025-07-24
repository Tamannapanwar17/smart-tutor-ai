# 📚 LearnLoop – Your Personal Offline AI Tutor

**LearnLoop** is a private, offline, intelligent tutor that helps you learn smarter — no APIs, no cloud, no tracking. Powered by open-source LLMs like Mistral or LLaMA, it adapts to your learning style, remembers your questions, and provides contextual, real-time answers.

> ✨ 100% Local. Fully Private. Internet-Free AI Tutoring.

---

![screenshot](./screenshot.png)

---

## 🌟 Key Highlights

✅ **Runs 100% Locally** — No OpenAI, no API keys  
✅ **Learns Over Time** — Personalized with memory via ChromaDB  
✅ **Fast, Responsive UI** — Built with Next.js + Tailwind CSS  
✅ **Powered by Ollama** — Easily run Mistral or LLaMA models locally  
✅ **Built for Hackathons** — Lightweight, simple, and fast to deploy

---

## 🖥️ Web App Overview

| Layer        | Technology Used              |
|--------------|------------------------------|
| 🌐 Frontend  | Next.js + Tailwind CSS        |
| ⚙️ Backend   | FastAPI (Python)              |
| 🧠 AI Engine | Ollama (Local LLM: Mistral)   |
| 🗂️ Memory    | ChromaDB (Vector DB)          |

---

## 🚀 Run the App Locally (in 4 Steps)

> 🛑 No internet or cloud services needed after setup.
# 1. Clone the repo
git clone https://github.com/Tamannapanwar17/smart-tutor-ai.git
cd smart-tutor-ai

# 2. Set up backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
# Visit: http://localhost:8000

# 3. Set up frontend
cd ../frontend
npm install
npm run dev
# Visit: http://localhost:3000

# 4. Start Ollama and run model
ollama run mistral
