# System-Prompt-Routing

# 🤖 System Prompt Routing (Beginner)

## 📌 Business Problem
When building multi-capability AI apps (e.g., apps that can **write code, summarize videos, or answer legal questions**), the prompts you send to the LLM often need to change depending on the user’s query.  

Instead of **manually switching prompts**, a **System Prompt Router** automatically finds and selects the best system prompt for the query using semantic similarity.

This project demonstrates how to build a simple but effective **System Prompt Router** from scratch.

---

## 🛠️ Key Steps

1. 📚 **Create a prompt library**  
   - Store prompts in a Python dictionary with descriptive keys.  

2. 🔍 **Embed system prompts**  
   - Use [sentence-transformers](https://www.sbert.net/) to embed prompt descriptions.  

3. 💬 **Handle user queries**  
   - Embed the incoming user query using the same model.  

4. 📊 **Find best match**  
   - Compare embeddings with [FAISS](https://faiss.ai/) for efficient similarity search.  
   - Select the system prompt with the **highest similarity score**.

---

## ⚙️ Tech Stack

- **[FAISS](https://faiss.ai/)** → For fast similarity search.  
- **[Sentence-Transformers](https://www.sbert.net/)** → For generating embeddings.  
- **[FastAPI](https://fastapi.tiangolo.com/)** → Backend API for handling queries.  
- **[Streamlit](https://streamlit.io/)** → Frontend UI for user interaction.  
- **[Docker](https://www.docker.com/)** → To containerize and run the entire project seamlessly.  

---

## 📂 Project Structure
System-Prompt-Routing/
│── backend_fastapi.py # FastAPI backend logic
│── app.py # Streamlit frontend UI
│── build_faiss.py # Script to build FAISS index
│── prompt_meta.pkl # Stored prompt metadata
│── prompt_index.faiss # FAISS index file
│── requirements.txt # Python dependencies
│── Dockerfile.backend # Dockerfile for backend
│── Dockerfile.frontend # Dockerfile for frontend
│── docker-compose.yml # Compose to run multi-container setup
└── README.md # Project documentation


---

## 🚀 How It Works

1. User enters a **query** in the Streamlit UI.  
2. The frontend calls the FastAPI backend (`/route_prompt`).  
3. Backend computes embeddings and performs **nearest-neighbor search with FAISS**.  
4. The **best matching system prompt** is returned and displayed with similarity score.  

---

## 🐳 Running with Docker

Build and run using Docker Compose:

``
# Build images and start containers
docker compose up --build -d

# Stop containers
docker compose down


#Example Output
User Query: "Can you assist me in writing Python code?"
✅ Best Match: "Code Assistant"
System Prompt: "You are an expert Python assistant..."
Score: 0.8932









