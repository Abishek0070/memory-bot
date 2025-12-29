import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage



llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)

SYSTEM_PROMPT = SystemMessage(
    content="You are a helpful assistant. Answer clearly."
)

st.title(" Groq Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = [SYSTEM_PROMPT]


for msg in st.session_state.chat:
    if isinstance(msg, HumanMessage):
        st.markdown(f"**You:** {msg.content}")
    elif msg != SYSTEM_PROMPT:
        st.markdown(f"**Bot:** {msg.content}")

user_input = st.text_input("Ask a question:")

if st.button("Ask") and user_input:
    with st.spinner("Thinking..."):
        st.session_state.chat.append(HumanMessage(content=user_input))

        response = llm.invoke(st.session_state.chat)
        st.session_state.chat.append(response)

        st.rerun() 





