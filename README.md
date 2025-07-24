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

![LearnLoop UI](./screenshot.png) <!-- Add your UI screenshot here -->

---

## 🧑‍💻 Tech Stack

| Layer        | Tech              |
|--------------|-------------------|
| Frontend     | Next.js, Tailwind CSS |
| Backend      | FastAPI (Python)  |
| AI Model     | Ollama (Mistral / LLaMA) |
| Memory Store | ChromaDB (local)  |

---

## ⚙️ Installation & Run (No API Keys Needed)

### 🪜 1. Clone the Repository

git clone https://github.com/Tamannapanwar17/learnloop-ai-tutor.git
cd learnloop-ai-tutor

### 🧠 2. Install & Run Ollama (Local LLM)
curl -fsSL https://ollama.com/install.sh | sh
ollama run mistral

### 🧩 3. Start Backend (Python + FastAPI)
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

### 🌐 4. Start Frontend (Next.js)
cd frontend
npm install
npm run dev

