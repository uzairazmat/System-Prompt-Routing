# app.py
import streamlit as st
import requests

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="Prompt Router with FAISS", page_icon="🤖")
st.title("🔍 Prompt Router (FAISS + FastAPI)")
st.write("Enter your query below, and I'll find the best matching system prompt.")

# -----------------------
# Input
# -----------------------
query = st.text_input("💬 Enter your query:")

# -----------------------
# Backend URL
# -----------------------
BACKEND_URL = "http://backend:8000/route_prompt"


# -----------------------
# Search Button
# -----------------------
if st.button("Find Prompt"):
    if query.strip() == "":
        st.warning("Please enter a query!")
    else:
        st.info(f"Searching best match for: **{query}** ...")
        try:
            response = requests.post(BACKEND_URL, json={"query": query})
            if response.status_code == 200:
                data = response.json()
                st.success(f"✅ Best Match: **{data['best_match']}**")
                st.write("**System Prompt:**")
                st.code(data['system_prompt'], language="markdown")
                st.caption(f"Score: {data['score']:.4f}")
            else:
                st.error("❌ Error from backend")
        except Exception as e:
            st.error(f"⚠️ Could not connect to backend: {e}")
