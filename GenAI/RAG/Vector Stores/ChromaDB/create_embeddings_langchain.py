import os
from langchain_text_splitters.html import HTMLHeaderTextSplitter
import chromadb
import rich as r
import uuid
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

parentDir = os.path.dirname(os.path.abspath(__file__))

splitter = HTMLHeaderTextSplitter(
    [("h1", "Header 1"), ("h2", "Header 2"), ("h2", "Header 2"), ("h2", "Header 2")]
)

with open(os.path.join(parentDir, r"html_pages/python_gil.html"), mode="r", encoding="utf-8") as f:
    
    chunks = splitter.split_text_from_file(f)


# create persistent Client
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DB")
chroma_client = chromadb.PersistentClient(path=db_path)

pythonCollection = chroma_client.get_or_create_collection("pythonCollection", embedding_function=SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-base-en-v1.5", local_files_only=True))

pythonCollection.upsert(
    ids=[str(uuid.uuid4())  for i in range(len(chunks))],
    # metadatas=[chunk.metadata for chunk in chunks],
    documents=[chunk.page_content for chunk in chunks]
)

