from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):

    query :str



@app.get("/")
def read_root():
    return {"Hello": "World"}



import faiss, pickle
import numpy as np
from sentence_transformers import SentenceTransformer

@app.on_event("startup")
def load_resources():
    """
    This function runs ONCE when FastAPI starts.
    We load FAISS index, metadata (keys/prompts), and embedding model.
    """
    global index, keys, prompts, model

    # Load FAISS index (created in build_faiss.py)
    index = faiss.read_index("prompt_index.faiss")

    # Load keys and prompt texts
    with open("prompt_meta.pkl", "rb") as f:
        meta = pickle.load(f)
    keys = meta["keys"]        # ordered list of keys
    prompts = meta["prompts"]  # dict of {key: prompt_text}

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")



@app.post("/route_prompt")
def route_prompt(req: QueryRequest):
    """
    Takes a user query, finds best matching prompt from FAISS index.
    """
    q = req.query  # user query

    # 1. Encode query
    q_emb = model.encode([q], convert_to_numpy=True).astype("float32")
    q_emb = q_emb / np.linalg.norm(q_emb, axis=1, keepdims=True)

    # 2. Search FAISS (top 1)
    D, I = index.search(q_emb, 1)  # D = scores, I = indices
    idx = I[0][0]

    # 3. Handle case when nothing found
    if idx == -1:
        return {
            "query": q,
            "best_match": None,
            "system_prompt": None,
            "score": None
        }

    # 4. Return best match
    key = keys[idx]
    return {
        "query": q,
        "best_match": key,
        "system_prompt": prompts[key],
        "score": float(D[0][0])
    }


