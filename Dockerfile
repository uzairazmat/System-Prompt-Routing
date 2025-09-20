# -----------------------
# 1. Base Image
# -----------------------
FROM python:3.11-slim


# -----------------------
# 2. Set Working Directory
# -----------------------
WORKDIR /app

# -----------------------
# 3. Install Dependencies
# -----------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------
# 4. Copy Project Files
# -----------------------
COPY . .

# -----------------------
# 5. Expose Port
# -----------------------
EXPOSE 8000

# -----------------------
# 6. Run FastAPI Server
# -----------------------
CMD ["uvicorn", "backend_faiss:app", "--host", "0.0.0.0", "--port", "8000"]
