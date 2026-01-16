import streamlit as st
import time
import jwt
import os
from extra_streamlit_components import CookieManager
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# 1. Setup
load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET", "change-this-to-a-strong-secret-in-production") 

try:
    llm = ChatGroq(
        model="llama-3.1-8b-instant", 
        temperature=0.2,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
except:
    st.error("GROQ_API_KEY not found. Please check your .env file.")


cookie_manager = CookieManager()

# --- THE UI STARTS HERE (Ensures sidebar is always visible) ---
st.set_page_config(page_title="Memory-BOT", layout="wide")
st.title("🧠 Bot")

with st.sidebar:
    st.header("Memory Status")
    status_placeholder = st.empty()
    status_placeholder.info("Searching for Memory Token...")

#  Memory Functions
def get_token_memory():
    # We add a small delay because CookieManager is slow
    time.sleep(0.2)
    token = cookie_manager.get("chat_memory")
    if token:
        try:
            return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])["summary"]
        except:
            return None
    return None

def save_token_memory(summary):
    new_token = jwt.encode({"summary": summary}, JWT_SECRET, algorithm="HS256")
    cookie_manager.set("chat_memory", new_token, key="save_token")

# 4. Logic to Restore Memory
past_summary = get_token_memory()

if past_summary:
    status_placeholder.success("✅ Memory Found in JWT")
else:
    # If no summary, we wait once and rerun to give browser time
    if "has_retried" not in st.session_state:
        st.session_state.has_retried = True
        time.sleep(0.8)
        st.rerun()
    status_placeholder.warning("⚠️ No Memory Found")

# 5. Initialize Chat History
if "chat" not in st.session_state:
    context = "You are a helpful assistant."
    if past_summary:
        context += f" Remember this project context: {past_summary}"
    st.session_state.chat = [SystemMessage(content=context)]

# 6. Display Chat
for msg in st.session_state.chat:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"): st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"): st.write(msg.content)

# 7. Input
user_input = st.chat_input("Ask about anything..")

if user_input:
    st.session_state.chat.append(HumanMessage(content=user_input))
    with st.chat_message("user"): st.write(user_input)

    with st.chat_message("assistant"):
        response = llm.invoke(st.session_state.chat)
        st.write(response.content)
        st.session_state.chat.append(AIMessage(content=response.content))

    # Save to JWT every time for this test
    summary_prompt = "Summarize the chat details discussed so far in 30 words."
    summary_res = llm.invoke(st.session_state.chat + [HumanMessage(content=summary_prompt)])
    save_token_memory(summary_res.content)
    st.toast("Memory Token Updated!")
    time.sleep(1) # Give cookie time to save before rerun
    st.rerun()



