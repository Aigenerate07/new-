import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Set page config
st.set_page_config(page_title="AI Assistant", page_icon="🤖")

# Initialize the agent
@st.cache_resource
def get_agent():
    return Agent(
        model=Groq(id="llama-3.3-70b-versatile", api_key='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'),
        tools=[DuckDuckGo()],
        show_tools_calls=True,
        markdown=True
    )

# Add a title
st.title("AI Assistant")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get AI response
    with st.chat_message("assistant"):
        agent = get_agent()
        response = agent.run(prompt)
        st.markdown(response.content)
    st.session_state.messages.append({"role": "assistant", "content": response.content})

