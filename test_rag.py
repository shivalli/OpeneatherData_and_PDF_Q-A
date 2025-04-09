from rag import answer_pdf_query

def test_rag_query():
    response = answer_pdf_query("What is the PDF about?")
    assert isinstance(response, str)
    assert len(response) > 10
