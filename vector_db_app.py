from flask import Flask, request, render_template
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

app = Flask(__name__)

# Load Sentence Transformer Model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Use a better generator model
text_generator = pipeline("text-generation", model="gpt2-large")

# Function to generate useful sentences based on query
def generate_sentences(query, num_sentences=5):
    generated = text_generator(query, max_length=70, num_return_sequences=num_sentences, do_sample=True, top_k=50, top_p=0.95, temperature=0.8)

    sentences = [text["generated_text"].strip() for text in generated]

    
    # Filter out incomplete or too short sentences
    sentences = [s for s in sentences if len(s.split()) > 5]
    return sentences

@app.route("/", methods=["GET", "POST"])
def search_page():
    results = []
    
    if request.method == "GET":
        return render_template("index.html", results=[])
    
    if request.method == "POST":
        query = request.form["query"]
        
        # Generate sentences
        sentences = generate_sentences(query)
        print("Generated Sentences:", sentences)  # Debug

        if not sentences:
            results.append(("Sorry, I couldn’t generate anything meaningful for your question. Please try rephrasing.", 0.0))
            return render_template("index.html", results=results)

        # Encode sentences
        sentence_vectors = model.encode(sentences)
        faiss.normalize_L2(sentence_vectors)

        dimension = sentence_vectors.shape[1]
        vector_index = faiss.IndexFlatIP(dimension)
        vector_index.add(sentence_vectors)

        # Encode and normalize query
        query_vector = model.encode([query])
        faiss.normalize_L2(query_vector)

        # Search
        _, indices = vector_index.search(query_vector, 5)
        threshold = 0.7  # Lowered threshold for more flexible matching

        # Collect results above threshold
        results = [
            (sentences[i], float(np.dot(query_vector, sentence_vectors[i].T)))
            for i in indices[0]
            if np.dot(query_vector, sentence_vectors[i].T) >= threshold
        ]

        # If still no good results
        if not results:
            results.append(("Hmm, I couldn’t find anything that matches closely. Try again with more details!", 0.0))

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)