# Document-Based Q&A with LangChain & Google Gemini  

This project demonstrates how to use **LangChain** with **Google Gemini** for building a simple document-based Q&A system. It loads a document, processes it into chunks, stores embeddings in FAISS, and retrieves answers using Gemini AI.  

## Features  
- Load and split a document into chunks  
- Generate embeddings using Google Gemini  
- Store embeddings in a FAISS vector database  
- Use a retrieval-based model to answer queries  

## Requirements  
- Python 3.8+  
- Install dependencies:  
  ```sh
  pip install -r requirements.txt
  ```  

## Setup  
1. Add your **Google API Key** in a `.env` file (copy from `.env.example`):  
   ```plaintext
   GOOGLE_API_KEY=your_api_key_here
   ```  
2. Place your document in `my_document.txt`.  
3. Run the script:  
   ```sh
   python script.py
   ```
