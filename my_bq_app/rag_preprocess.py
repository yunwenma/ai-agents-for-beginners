import os
import fitz  # PyMuPDF
import re
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

def split_into_chunks(text, chunk_size=400):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def embed_and_store(chunks, collection_name):
    model_name = 'paraphrase-multilingual-MiniLM-L12-v2'
    model = SentenceTransformer(model_name)
    
    chroma_client = chromadb.Client()
    chroma_collection = chroma_client.create_collection(
        name=collection_name,
        embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
    )

    for i, chunk in enumerate(chunks):
        chroma_collection.add(
            documents=[chunk],
            ids=[f"{collection_name}-{i}"]
        )
    print(f"✅ Successfully stored {len(chunks)} chunks into Chroma collection: {collection_name}")

if __name__ == "__main__":
    pdf_path = "/workspaces/ai-agents-for-beginners/my_bq_app/bqclass.pdf"
    collection_name = "bq_chunks"

    print("📖 Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("✂️ Splitting text into chunks...")
    chunks = split_into_chunks(text)

    print("📦 Embedding and storing in ChromaDB...")
    embed_and_store(chunks, collection_name)