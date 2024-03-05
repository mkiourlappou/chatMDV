# LangChain
from langchain.llms import VertexAI
from langchain.embeddings import VertexAIEmbeddings

from langchain.schema import HumanMessage, SystemMessage
from langchain.schema.document import Document

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.text_splitter import Language

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from typing import List
from pydantic import BaseModel

# Vertex AI
from google.cloud import aiplatform
import vertexai

# Streamlit
import streamlit as st

# Other
import os
from pprint import pprint
import requests, time

import google.auth

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "/Users/maria/.config/gcloud/application_default_credentials.json"  # key_path
)

vertexai.init(project="fine-cycling-414213")  # st.secrets["file_id"])

GITHUB_TOKEN = "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"  # st.secrets["github_token"]  # @param {type:"string"}
GITHUB_REPO = "mkiourlappou/chatMDV"  # @param {type:"string"}


### LLM
code_llm = VertexAI(
    model_name="code-bison@002",
    max_output_tokens=2048,
    temperature=0.1,
    verbose=False,
)


# Crawls a GitHub repository and returns a list of all ipynb files in the repository
def crawl_github_repo(url, is_sub_dir, access_token=f"{GITHUB_TOKEN}"):

    ignore_list = ["__init__.py"]

    if not is_sub_dir:
        api_url = f"https://api.github.com/repos/{url}/contents"
    else:
        api_url = url

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Check for any request errors

    files = []

    contents = response.json()

    for item in contents:
        if (
            item["type"] == "file"
            and item["name"] not in ignore_list
            and (item["name"].endswith(".py") or item["name"].endswith(".ipynb"))
        ):
            files.append(item["html_url"])
        elif item["type"] == "dir" and not item["name"].startswith("."):
            sub_files = crawl_github_repo(item["url"], True)
            time.sleep(0.1)
            files.extend(sub_files)

    return files


code_files_urls = crawl_github_repo(GITHUB_REPO, False, GITHUB_TOKEN)

# Write list to a file so you do not have to download each time
with open(
    "/Users/maria/Documents/wellcome_human_gen_project/ChatBioinformatics/code_files_urls_chatBio.txt",
    "w",
) as f:
    for item in code_files_urls:
        f.write(item + "\n")


# Extracts the python code from an .py file from github
def extract_python_code_from_py(github_url):
    raw_url = github_url.replace("github.com", "raw.githubusercontent.com").replace(
        "/blob/", "/"
    )
    response = requests.get(raw_url)
    response.raise_for_status()  # Check for any request errors

    python_code = response.text

    return python_code


with open(
    "/Users/maria/Documents/wellcome_human_gen_project/ChatBioinformatics/code_files_urls_chatBio.txt"
) as f:
    code_files_urls = f.read().splitlines()

code_strings = []

for i in range(0, len(code_files_urls)):
    if code_files_urls[i].endswith(".py"):
        content = extract_python_code_from_py(code_files_urls[i])
        doc = Document(
            page_content=content, metadata={"url": code_files_urls[i], "file_index": i}
        )
        code_strings.append(doc)

# Chunk code strings
text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=1500, chunk_overlap=150
)
texts = text_splitter.split_documents(code_strings)

EMBEDDING_QPM = 100
EMBEDDING_NUM_BATCH = 5
embeddings = VertexAIEmbeddings(
    requests_per_minute=EMBEDDING_QPM,
    num_instances_per_batch=EMBEDDING_NUM_BATCH,
    model_name="textembedding-gecko@latest",
)

# Create Index from embedded code chunks
db = FAISS.from_documents(texts, embeddings)

# Init your retriever.
retriever = db.as_retriever(
    search_type="similarity",  # Also test "similarity", "mmr"
    search_kwargs={"k": 5},
)

# RAG template
prompt_RAG = """
    You are a proficient python developer. Respond with the syntactically correct python code to the {question} below. Make sure you follow these rules:
    1. Base the structure of the python code on the structure of files in the {context}
    2. Generate the contents of a python file that serves an MDV project
    
    Context:
    {context}

    """

prompt_RAG_template = PromptTemplate(
    template=prompt_RAG, input_variables=["context", "question"]
)

qa_chain = RetrievalQA.from_llm(
    llm=code_llm,
    prompt=prompt_RAG_template,
    retriever=retriever,
    return_source_documents=True,
)

### Streamlit components
st.set_page_config(
    page_title="Ask MDV to generate a graph", page_icon="🦜🔗", layout="wide"
)

st.title("Ask MDV to generate a graph")


# check for messages in session and create if not exists
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "What type of MDV graph would you like to generate?",
        }
    ]

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response_all = qa_chain({"query": user_prompt})
            ai_response = ai_response_all["result"]
            st.write(ai_response)
    new_ai_message = {"role": "assistant", "content": ai_response}
    st.session_state.messages.append(new_ai_message)
