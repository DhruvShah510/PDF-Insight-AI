# PDF-Insight-AI
Ask questions from any PDF instantly using AI. Upload a PDF , and get smart answers powered by LLMs. Built with Python, Streamlit, and LangChain.
A Streamlit-based web app that lets you **ask questions about your PDF** documents using LLMs and vector-based retrieval. Upload a PDF (max 20 pages), and ask anything about its contents – answers are generated contextually using a custom RAG (Retrieval-Augmented Generation) pipeline.


## 🚀 Features

- ✅ Upload and parse PDFs (up to 20 pages)
- 🔍 Chunk and embed PDF content using **MiniLM embeddings**
- 🧠 Query-relevant chunks retrieved using **FAISS vector search**
- 💬 Answers generated using **FLAN-T5 (via Hugging Face)**
- ⚡ Built with LangChain and Streamlit

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: LangChain + Hugging Face Transformers  
- **Embeddings**: `all-MiniLM-L6-v2` (Sentence Transformers)  
- **LLM**: `google/flan-t5-base`  
- **Vector DB**: FAISS



## 📂 Project Structure

- app.py # Streamlit UI
- pdf_qa_engine.py # Core RAG pipeline
- requirements.txt # Python dependencies
- README.md # This file
- model_creation_process.ipynb # complete process steps file
- final_code.ipynb # final code file without streamlit
- LICENCE # licence file
- .gitignore
  
## 📦 Installation
- **Clone the repo**: git clone https://github.com/DhruvShah510/PDF-Insight-AI.git
- **(Optional) Create virtual environment** : python -m venv venv
- **activate virtual environment** : source venv/bin/activate    # On Windows: venv\Scripts\activate
- **install dependencies** : pip install -r requirements.txt

## ▶️ Usage
- Run the app with: streamlit run app.py
- Upload a PDF (≤ 20 pages)
- Ask a question
- Get an answer based on the document content

## ⚠️ Limitations
- PDF must be 20 pages or fewer
- Works best for short factual questions
- Large, complex documents may need better chunking or fine-tuned models

## 📃 License
This project is open-sourced under the MIT License.

## 🙋‍♂️ Author
Dhruv Shah

## ⭐️ Star the Repo
If you found this useful, don't forget to ⭐️ star the repo on GitHub!


