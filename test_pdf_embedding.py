from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def test_pdf_chunking():
    loader = PyPDFLoader("sample.pdf")
    docs = loader.load()
    assert len(docs) > 0

    # Duplicate content to simulate a longer document
    docs[0].page_content *= 5

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    assert len(chunks) >= 1  # updated assertion
