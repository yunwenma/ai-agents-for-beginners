# rag_utils.py
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

# 初始化嵌入模型与 Chroma 客户端
model_name = 'paraphrase-multilingual-MiniLM-L12-v2'
model = SentenceTransformer(model_name)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
chroma_client = chromadb.Client()
collection = chroma_client.get_collection(name="bq_chunks", embedding_function=embedding_func)

def retrieve_relevant_chunks(text, top_k=3):
    """
    Given a question or user input, retrieve top_k most relevant chunks
    from the embedded PDF collection.
    """
    results = collection.query(query_texts=[text], n_results=top_k)
    documents = results.get("documents", [[]])[0]
    return documents