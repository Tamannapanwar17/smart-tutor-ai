# smart-tutor-ai
**LearnLoop** is an open-source, fully local AI tutor that adapts to each student’s learning style. It remembers what you've asked, tracks your progress, and adjusts its explanations in real time — no internet APIs or paid services required!
mkdir learnloop-ai-tutor
cd learnloop-ai-tutor
mkdir backend
cd backend
touch app.py
  from fastapi import FastAPI
  from fastapi.middleware.cors import CORSMiddleware
  
  app = FastAPI()
  
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )
  
  @app.get("/")
  async def root():
      return {"message": "LearnLoop Backend is running!"}
touch requirements.txt
  fastapi
  uvicorn
  chromadb
pip install -r requirements.txt
uvicorn app:app --reload
cd ..
npx create-next-app@latest frontend --typescript
cd frontend
  export default function Home() {
    return (
      <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
        <h1>👋 Welcome to LearnLoop AI Tutor</h1>
        <p>This is your personal offline AI learning assistant!</p>
      </div>
    );
  }
npm install
npm run dev
curl -fsSL https://ollama.com/install.sh | sh
ollama run mistral
touch .gitignore
  # Node
  frontend/node_modules/
  frontend/.next/
  frontend/.env
  
  # Python
  __pycache__/
  *.pyc
  *.pyo
  *.pyd
  env/
  venv/
  backend/.env
  
  # System
  .DS_Store
  Thumbs.db
  
  # IDE
  .vscode/
  .idea/
touch README.md
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
git clone https://github.com/YourUsername/learnloop-ai-tutor.git
cd learnloop-ai-tutor
![LearnLoop UI](./screenshot.png)
git init
git add .
git commit -m "Initial commit for LearnLoop AI"
gh repo create learnloop-ai-tutor --public --source=. --push








