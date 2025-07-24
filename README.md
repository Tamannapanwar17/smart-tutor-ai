# smart-tutor-ai

**LearnLoop** is an open-source, fully local AI tutor that adapts to each student’s learning style. It remembers what you've asked, tracks your progress, and adjusts its explanations in real time — no internet APIs or paid services required!

> 📍 Runs completely offline using open-source AI models and vector databases.

---

## 🚀 Features

* ✅ **Offline AI Tutor** – No OpenAI or paid APIs required
* ✅ **Local LLM (Ollama)** – Lightweight models like Mistral or LLaMA run on your device
* ✅ **Memory & Feedback Loop** – Tracks previous questions and adapts responses
* ✅ **ChromaDB** – Stores and retrieves your learning history
* ✅ **Fully Web-Based Interface** – Built with Next.js + Tailwind CSS
* ✅ **Hackathon-Ready** – Easy to set up and run locally

---

## 🖼️ Demo Screenshot

![LearnLoop UI](./screenshot.png) <!-- Optional: Replace with actual screenshot -->

---

## 🧑‍💻 Tech Stack

| Layer        | Tech                     |
| ------------ | ------------------------ |
| Frontend     | Next.js, Tailwind CSS    |
| Backend      | FastAPI (Python)         |
| AI Model     | Ollama (Mistral / LLaMA) |
| Memory Store | ChromaDB (local)         |

---

## ⚙️ Installation & Run Locally (No API Keys Needed)

### 🧼 1. Clone the Repository

```bash
git clone https://github.com/Tamannapanwar17/learnloop-ai-tutor.git
cd learnloop-ai-tutor
```

### 📚 2. Setup Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
uvicorn app:app --reload
```

Visit [http://localhost:8000](http://localhost:8000) to check if backend is running.

### 🌐 3. Setup Frontend

```bash
cd ../frontend
npm install
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to view the app UI.

### 🧒 4. Run AI Model with Ollama

```bash
ollama run mistral
```

If not installed:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## 🔧 Development Tips

* Make sure FastAPI is running on port `8000`
* Ensure Ollama is active before asking AI questions
* Adjust `frontend/pages/index.tsx` if routing fails

---

## 🔮 Initialize Git & Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit for LearnLoop AI"
gh repo create learnloop-ai-tutor --public --source=. --push
```

GitHub Repo: [Tamannapanwar17/learnloop-ai-tutor](https://github.com/Tamannapanwar17/learnloop-ai-tutor)

---

## 📊 Future Features (Optional)

* [ ] Local user authentication
* [ ] Quiz generation from topics
* [ ] Text-to-speech replies
* [ ] AI-graded answers

---

## 🙏 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

---

## ✅ License

[MIT License](LICENSE)

