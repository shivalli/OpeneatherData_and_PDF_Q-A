# OpeneatherData_and_PDF_Q-A
An intelligent assistant that can:  🔍 Answer questions from PDF documents using Retrieval-Augmented Generation (RAG) that can fetch real-time weather data for any city also provides a chat-based UI using Streamlit
Powered by:

LangChain for orchestration

Groq API for LLM

Qdrant Cloud for vector storage

OpenWeatherMap API for weather data

Project Structure:
project/
│
├── app.py                # Streamlit UI
├── rag.py                # PDF loader + RAG logic using Groq + Qdrant
├── weather.py            # Real-time weather fetching logic
├── decision.py           # Query classifier (weather vs. PDF)
├── sample.pdf            # Sample document for RAG
├── .env                  # API keys
├── requirements.txt      # Python dependencies
└── README.md             # You're here!


Install Python dependencies:
pip install -r requirements.txt
langchain

langchain-groq

qdrant-client

sentence-transformers

torch

pypdf

streamlit

requests

python-dotenv

fpdf (optional for generating test PDFs)

 Add .env file
 GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
QDRANT_URL=https://your-cluster.qdrant.cloud
QDRANT_API_KEY=your_qdrant_api_key
Add a sample PDF
pip install fpdf
python generate_sample_pdf.py
Run the App
