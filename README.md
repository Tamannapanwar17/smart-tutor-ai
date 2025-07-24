# 📚 smart-tutor-ai — *LearnLoop*

**LearnLoop** is a local-first AI tutor that works entirely offline on Windows — no internet, no APIs, no cloud. It adapts to your learning style, remembers your questions, and runs inside your browser via a clean local web interface.

> ✅ Powered by local LLMs (like Mistral) and vector memory (ChromaDB)  
> ✅ Open in Chrome at `http://localhost:3000`

---

## 🌟 Features

- ✅ **Runs Fully Offline** – No API keys or internet required
- ✅ **Local AI Models** – Uses Mistral/LLaMA via [Ollama](https://ollama.com)
- ✅ **Learner Memory** – Stores and recalls previous interactions with ChromaDB
- ✅ **Modern UI** – Access via browser with Next.js frontend
- ✅ **Built for Windows** – Quick setup via terminal
- ✅ **Optional Web UI** – Can use [Open WebUI](https://github.com/open-webui/open-webui) for simpler Chrome access

---

## 🛠️ Tech Stack

| Layer         | Technology            |
|---------------|------------------------|
| Frontend UI   | Next.js + Tailwind CSS |
| Backend API   | FastAPI (Python)       |
| AI Models     | Ollama + Mistral       |
| Memory Engine | ChromaDB (local)       |
| Optional UI   | Open WebUI (Docker)    |

---

## ⚙️ Setup Instructions for Windows

> 💡 You only need to follow one path:  
> Either use **manual setup** (for full control) or **Open WebUI** (for Chrome access instantly).

---

### 🔧 OPTION 1: Manual Setup (Advanced, Full Control)

1. **Install Ollama**  
   Download and install: [https://ollama.com/download](https://ollama.com/download)  
   Test with:
   ```bash```
   ollama run mistral
git clone https://github.com/Tamannapanwar17/smart-tutor-ai.git
cd smart-tutor-ai/backend

python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn app:app --reload    # Runs at http://localhost:8000
cd smart-tutor-ai/frontend
npm install
npm run dev                 # Open http://localhost:3000 in Chrome

