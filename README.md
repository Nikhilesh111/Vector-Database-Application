Vector Search App with GPT-2 and FAISS
This project is a web-based application that generates and searches for semantically similar sentences based on user queries. It utilizes GPT-2 (large) for sentence generation, Sentence Transformers for encoding sentences into vector embeddings, and FAISS for efficient similarity search in high-dimensional vectors.

Features
Sentence Generation: Generate meaningful sentences related to the user's query using the GPT-2 model.

Semantic Search: Convert generated sentences to vector embeddings using Sentence Transformers.

Efficient Search: Perform fast and accurate similarity search with FAISS, which handles large-scale high-dimensional vector searches.

Web Interface: A simple and intuitive Flask-based web interface for submitting queries and displaying the most relevant results.

Technologies Used:
Flask: Lightweight web framework to create the server and handle requests.

GPT-2 (large): A large pre-trained language model by OpenAI used for generating sentences based on input queries.

Sentence Transformers: Python library for converting sentences into vector embeddings that capture semantic meaning.

FAISS: Facebook AI Similarity Search, designed to handle fast similarity searches in high-dimensional spaces.

Hugging Face Transformers: For loading and utilizing the GPT-2 model for text generation.

How It Works
Generate Sentences: When the user submits a query, the app uses GPT-2 to generate a list of sentences related to the query.

Convert to Vectors: The generated sentences are then converted to vector embeddings using SentenceTransformers.

Store Vectors in FAISS: The sentence vectors are indexed using FAISS, enabling efficient similarity search.

Search for Similar Sentences: The app encodes the user's query into a vector, searches the FAISS index for the most similar sentences, and returns the results along with a similarity score.

How to Run Locally
Prerequisites
Python 3.7+

Pip (for installing dependencies)

Steps to Set Up:
Create a Virtual Environment and Activate it:
python3 -m venv venv
source venv/bin/activate  
# On Windows, use: venv\Scripts\activate

Install Required Libraries:
pip install -r requirements.txt

Run the Flask App:
python vector_db_app.py

To access the web interface, visit the following URL in the browser: http://127.0.0.1:5000/.

Usage
Enter the query in the search box and press Search.

The app will generate related sentences and display the top 5 most semantically similar sentences based on your input.

The similarity score for each result will also be displayed.

Technologies Used:
Flask: Lightweight web framework for Python.

GPT-2 (large): Pre-trained language model for text generation.

Sentence-Transformers: Library to convert sentences into embeddings.

FAISS: Facebook AI Similarity Search for efficient similarity search in high-dimensional vector spaces.
