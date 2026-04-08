import os
import chromadb
import rich as r
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

client = chromadb.PersistentClient()
embedding_function = SentenceTransformerEmbeddingFunction(model_name="intfloat/e5-base-v2")

