import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []

index = faiss.IndexFlatL2(384)

def create_vector_store(text):

    chunks = text.split("\n")

    global documents
    documents = chunks

    embeddings = model.encode(chunks)

    index.add(
        np.array(embeddings).astype("float32")
    )

def retrieve(query):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype("float32"),
        k=3
    )

    retrieved = []

    for idx in I[0]:
        retrieved.append(documents[idx])

    return "\n".join(retrieved)