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

### 1️⃣ Clone the Repo
```bash``
git clone https://github.com/Tamannapanwar17/smart-tutor-ai.git
cd smart-tutor-ai
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app:app --reload  # Backend runs at http://localhost:8000
cd ../frontend
npm install
npm run dev  # Frontend runs at http://localhost:3000
# One-time install if not done:
curl -fsSL https://ollama.com/install.sh | sh

# Then run the model:
ollama run mistral  # Starts LLM at http://localhost:11434
git init
git add .
git commit -m "Initial commit for LearnLoop"
gh repo create smart-tutor-ai --public --source=. --push
