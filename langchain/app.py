import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

loader = TextLoader("my_document.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
db = FAISS.from_documents(texts, embeddings)

llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash", temperature=0.5)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())

queries = ["What is the main topic of the document?", "Give me a short summary"]
for query in queries:
    print(f"Q: {query}")
    print(f"A: {qa.invoke(query)}\n")
