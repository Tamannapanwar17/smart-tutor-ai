
# 📚 LearnLoop – Local AI Tutor

LearnLoop is a fully offline, privacy-focused AI tutor built for students in low-connectivity environments. It runs entirely on local hardware using [Ollama](https://ollama.com/) for LLM inference, [ChromaDB](https://www.trychroma.com/) for vector storage, and [Streamlit](https://streamlit.io/) or [Gradio](https://www.gradio.app/) for the user interface.

> 🔐 No cloud. No tracking. 100% local learning.

---

## 🚀 Features

- 🧠 **Offline LLM** with Ollama (supports LLaMA2, Mistral, etc.)
- 📁 **File Upload** – Ask questions based on your PDFs, text files, etc.
- 🔍 **Local RAG (Retrieval-Augmented Generation)** via ChromaDB
- 🧪 **FastAPI Backend** for modular API calls
- 🎨 **Streamlit or Gradio UI** for interactive tutoring
- 📤 **Export Q&A** to TXT or PDF
- ⚙️ **Runs entirely offline** – ideal for privacy and rural environments

---

## 🛠️ Tech Stack

| Layer          | Tool/Framework            |
|----------------|---------------------------|
| LLM Inference  | [Ollama](https://ollama.com/) |
| RAG/Vector DB  | [ChromaDB](https://www.trychroma.com/) |
| Backend APIs   | [FastAPI](https://fastapi.tiangolo.com/) |
| Frontend UI    | [Streamlit](https://streamlit.io/) / [Gradio](https://gradio.app/) |
| PDF Support    | `fpdf`, `PyMuPDF`         |

---

## 📦 Installation (Local)

```bash
git clone https://github.com/Tamannapanwar17/LearnLoop-AI-tutor.git
cd LearnLoop-AI-tutor

