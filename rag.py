import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "rag-weather-assistant"


qdrant = None

def load_pdf(file_path="sample.pdf"):
    global qdrant
    if qdrant is None:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        qdrant = Qdrant.from_documents(
            chunks,
            embeddings,
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
            collection_name="pdf_docs"
        )


def answer_pdf_query(query: str) -> str:
    load_pdf()
    retriever = qdrant.as_retriever()

    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0.7,
        api_key=os.getenv("GROQ_API_KEY"),
    )

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(query)
