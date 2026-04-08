import os
import chromadb
import rich as r
# creates in-memory client
# chroma_client = chromadb.Client() 

# create persistent Client
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DB")
chroma_client = chromadb.PersistentClient(path=db_path)

# let's create a collection
collection = chroma_client.get_or_create_collection("first_collection")

# adding some documents to the collection
documents = ["This is a document about pineapple",
             "This is a document about oranges"
            ]

# adding documents
# `add()` adds same document everytime you run the script
# collection.add(
#     ids = ["id1", "id2"],
#     documents=documents
# )
# use upsert to avoid adding same document again
collection.upsert(
    ids = ["id1", "id2"],
    documents=documents
)

results = collection.query(
    query_texts=["oranges"],
    n_results=1
)

r.print(results)