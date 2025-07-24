# 📚 smart-tutor-ai — *LearnLoop*

**LearnLoop** is a fully offline, open-source AI tutor that adapts to your learning style. It remembers what you ask, tracks progress, and gives smarter answers over time — with zero internet dependency.

> ✅ No API keys. No cloud. Just local AI magic on your machine.

---

## 🚀 Features

- ✅ **Runs 100% Locally** – No OpenAI or paid APIs  
- ✅ **Smart Local LLMs** – Uses Ollama + Mistral or LLaMA  
- ✅ **Learner Memory** – Remembers previous questions  
- ✅ **ChromaDB** – Vector search to personalize tutoring  
- ✅ **Modern UI** – Built with Next.js + Tailwind CSS  
- ✅ **Hackathon Ready** – Quick setup, works offline  

---

## 🧠 Demo Screenshot

![LearnLoop UI](./screenshot.png)  
<!-- Optional: Add actual screenshot or Loom/Youtube walkthrough -->

---

## 🛠️ Tech Stack

| Layer        | Tech Stack               |
|--------------|---------------------------|
| Frontend     | Next.js, Tailwind CSS     |
| Backend      | FastAPI (Python)          |
| AI Model     | Ollama + Mistral/LLaMA    |
| Memory Store | ChromaDB (local)          |

---

## ⚙️ Local Installation (No API Keys Needed)

Follow these **one-time setup steps**:

### 1. 📦 Clone the Project
```bash```
git clone https://github.com/Tamannapanwar17/smart-tutor-ai.git
cd smart-tutor-ai
cd backend

pip install -r requirements.txt
uvicorn app:app --reload
cd ../frontend
npm install
npm run dev
ollama run mistral
git init && git add . && git commit -m "Initial commit" && gh repo create smart-tutor-ai --public --source=. --push
