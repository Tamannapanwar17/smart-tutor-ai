# 📚 smart-tutor-ai — *LearnLoop*

**LearnLoop** is an open-source, fully offline AI tutor that adapts to your learning style. It remembers your questions, tracks progress, and provides smarter responses over time — all without internet, APIs, or cloud services.

> 🚀 Runs 100% locally using open-source AI models like Mistral and a vector database (ChromaDB).

---

## ✨ Features

- ✅ **No APIs, No Cloud** — Everything runs locally
- ✅ **Local LLMs with Ollama** — Use models like Mistral or LLaMA
- ✅ **Adaptive Memory** — Learns from your past questions
- ✅ **ChromaDB** — Stores and retrieves learning history
- ✅ **Modern UI** — Built with Next.js + Tailwind CSS
- ✅ **Hackathon Friendly** — Lightweight, fast to set up

---

## 🖼️ Demo Screenshot

![LearnLoop UI](./screenshot.png)

---

## 🛠️ Tech Stack

| Layer        | Tech Used              |
|--------------|------------------------|
| Frontend     | Next.js, Tailwind CSS  |
| Backend      | FastAPI (Python)       |
| AI Models    | Ollama + Mistral/LLaMA |
| Vector DB    | ChromaDB (local)       |

---

## ⚙️ Getting Started

### 1. 🔽 Clone the Repository

```bash```
git clone https://github.com/Tamannapanwar17/smart-tutor-ai.git
cd smart-tutor-ai
cd backend
python -m venv venv
venv\Scripts\activate           # Windows

pip install -r requirements.txt
uvicorn app:app --reload        # Runs on http://localhost:8000
cd ../frontend
npm install
npm run dev                     # Runs on http://localhost:3000
curl -fsSL https://ollama.com/install.sh | sh
chmod +x install_ollama.sh
ollama run mistral

git init
git add .
git commit -m "Initial commit for LearnLoop"
gh repo create smart-tutor-ai --public --source=. --push
