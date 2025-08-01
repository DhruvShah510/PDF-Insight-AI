# app.py

import streamlit as st
from pdf_qa_engine import PDFQuestionAnsweringEngine
import tempfile
import os

st.set_page_config(page_title="📄 PDF Q&A Assistant", layout="centered")

st.title("📚 PDF Question Answering App")
st.markdown("Upload a PDF (max 20 pages), ask any question about it!")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_pdf_path = tmp_file.name

    try:
        with st.spinner("Processing PDF..."):
            engine = PDFQuestionAnsweringEngine(temp_pdf_path)
            st.success("✅ PDF loaded successfully! Ask your questions below:")

            question = st.text_input("🧠 Enter your question:")

            if question:
                with st.spinner("Generating answer..."):
                    answer = engine.ask(question)
                    st.markdown(f"### 📌 Answer:\n{answer}")

    except FileNotFoundError:
        st.error("❌ Could not find the uploaded file.")
    except ValueError as ve:
        st.error(f"❌ {str(ve)}")
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred: {str(e)}")

# Remove default Streamlit footer
st.markdown("""
    <style>
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
