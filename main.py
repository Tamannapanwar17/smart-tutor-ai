from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

# Example ChromaDB integration (optional)
import chromadb
from chromadb.utils import embedding_functions

app = FastAPI()

# CORS settings (for frontend use)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models ---
class QuestionRequest(BaseModel):
    question: str

# --- ChromaDB Setup (Optional) ---
client = chromadb.Client()
collection = client.get_or_create_collection(
    name="learnloop-docs",
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
)

# --- Routes ---

@app.get("/")
def read_root():
    return {"message": "LearnLoop AI Tutor Backend is running."}

@app.post("/ask")
def ask_question(payload: QuestionRequest):
    # Basic LLM chat using Ollama (e.g., llama2 or mistral)
    ollama_response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": payload.question}
    )

    result = ollama_response.json()
    return {"answer": result.get("response", "No response received")}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    # Add to ChromaDB for embedding search
    collection.add(
        documents=[text],
        ids=[file.filename]
    )

    return {"message": f"{file.filename} uploaded and indexed."}
