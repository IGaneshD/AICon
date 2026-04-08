from create_embeddings_langchain import pythonCollection
import rich as r

results = pythonCollection.query(
    query_texts=("What is Python GIL?")
)

r.print(results)