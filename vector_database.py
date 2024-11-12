import faiss
import numpy as np
import embedding
import json

# Sample embeddings and metadata
texts = ["apple", "truck", "castle"]
embeddings = np.array([embedding.embedding(text) for text in texts])

print(embeddings.shape)

# Create a Faiss index
index = faiss.IndexFlatL2(embeddings.shape[1])

# Perform a similarity search
query_text = "car"
query_vector = np.array(embedding.embedding(query_text))
distances, indices = index.search(query_vector.reshape(1, -1), 3)

# Retrieve the top 2 most similar documents and their metadata
print(distances, indices)


class VectorDatabaseWraper:
    def __init__ (self, folder_path = None, embedding_size = 1536):
        if folder_path:
            self.index = faiss.read_index(f"{folder_path}/database.index")
            with open(f"{folder_path}/metadata.json", 'r') as infile:
                self.metadata = json.load(infile)
        else:
            self.index = faiss.IndexFlatL2(embedding_size)
            self.metadata = []

    def save(self, folder_path):
        faiss.write_index(self.index, f"{folder_path}/database.index")
        with open(f"{folder_path}/metadata.json", 'w') as outfile:
            json.dump(self.metadata, outfile)

    def add(self, embeddings, metadatas):
        self.index.add(embeddings)
        self.metadata.extend(metadatas)

    def search(self, query_vector, k):
        distances, indices = self.index.search(query_vector.reshape(1, -1), k)
        return distances, indices


        
    
        
    