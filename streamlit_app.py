import nest_asyncio
from llama_index.readers.github_readers.github_repository_reader import (
    GithubRepositoryReader,
)
import os
import streamlit_app as st
from llama_index.llms import OpenAI
import openai
from llama_index import VectorStoreIndex, ServiceContext

nest_asyncio.apply()
openai_key = os.getenv('OPENAI_API_KEY')

openai.api_key = st.secrets.openai_key
st.header("Chat with the medical pipeline assistant 💬 📚")

if "messages" not in st.session_state.keys(): 
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about SpOOx!"}
    ]

github_token = os.getenv('GITHUB_TOKEN')
owner = "mostafaosama999"
branch = "main"

@st.cache_resource(show_spinner=False)
def load_index():
    with st.spinner(text="Loading and indexing the spoox pipeline and other pipelines - hang tight! This should take 1-2 minutes."):
        # 1. Embeddings / OpenAI Usage
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-4-0125-preview", temperature=0.5, 
            system_prompt="You are an expert on medical pipelines that utilitse WDL, nextflow and ruffus. Keep your answers technical and based on facts – do not hallucinate features."))

        # 2. Data loader
        docs_SpOOx = GithubRepositoryReader(
                        github_token=github_token,
                        owner=owner,
                        repo="SpOOx",
                        use_parser=False,
                        verbose=True,
                    ).load_data(branch=branch)
        # 3. Index
        index = VectorStoreIndex.from_documents(docs_SpOOx,show_progress=True, service_context=service_context)
        return index

index = load_index()

# 4. ChatEngine
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # 5. Chat response generator
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) 
            
