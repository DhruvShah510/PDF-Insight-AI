# PDF-Insight-AI
Ask questions from any PDF instantly using AI. Upload a PDF , and get smart answers powered by LLMs. Built with Python, Streamlit, and LangChain.
A Streamlit-based web app that lets you **ask questions about your PDF** documents using LLMs and vector-based retrieval. Upload a PDF (max 20 pages), and ask anything about its contents – answers are generated contextually using a custom RAG (Retrieval-Augmented Generation) pipeline.

---

## 🚀 Features

- ✅ Upload and parse PDFs (up to 20 pages)
- 🔍 Chunk and embed PDF content using **MiniLM embeddings**
- 🧠 Query-relevant chunks retrieved using **FAISS vector search**
- 💬 Answers generated using **FLAN-T5 (via Hugging Face)**
- ⚡ Built with LangChain and Streamlit

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: LangChain + Hugging Face Transformers  
- **Embeddings**: `all-MiniLM-L6-v2` (Sentence Transformers)  
- **LLM**: `google/flan-t5-base`  
- **Vector DB**: FAISS

---

## 📂 Project Structure

- app.py # Streamlit UI
- pdf_qa_engine.py # Core RAG pipeline
- requirements.txt # Python dependencies
- README.md # This file

  


