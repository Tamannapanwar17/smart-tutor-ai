# smart-tutor-ai

**LearnLoop** is an open-source, fully local AI tutor that adapts to each student’s learning style. It remembers what you've asked, tracks your progress, and adjusts its explanations in real time — no internet APIs or paid services required!

> 📍 Runs completely offline using open-source AI models and vector databases.

---

## 🚀 Features

- ✅ **Offline AI Tutor** – No OpenAI or paid APIs required  
- ✅ **Local LLM (Ollama)** – Lightweight models like Mistral or LLaMA run on your device  
- ✅ **Memory & Feedback Loop** – Tracks previous questions and adapts responses  
- ✅ **ChromaDB** – Stores and retrieves your learning history  
- ✅ **Fully Web-Based Interface** – Built with Next.js + Tailwind CSS  
- ✅ **Hackathon-Ready** – Easy to set up and run locally  

---

## 🖼️ Demo Screenshot

![LearnLoop UI](./screenshot.png) <!-- Replace with actual screenshot if available -->

---

## 🧑‍💻 Tech Stack

| Layer        | Tech                  |
|--------------|-----------------------|
| Frontend     | Next.js, Tailwind CSS |
| Backend      | FastAPI (Python)      |
| AI Model     | Ollama (Mistral / LLaMA) |
| Memory Store | ChromaDB (local)      |

---

## ⚙️ Installation & Run Locally (No API Keys Needed)

### 🧼 1. Clone the Repository
```bash```
git clone https://github.com/Tamannapanwar17/smart-tutor-ai.git
cd smart-tutor-ai

cd backend
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
uvicorn app:app --reload
cd ../frontend
npm install
npm run dev
ollama run mistral
curl -fsSL https://ollama.com/install.sh | sh
git init
git add .
git commit -m "Initial commit"
gh repo create smart-tutor-ai --public --source=. --push
