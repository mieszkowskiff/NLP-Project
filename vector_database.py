import faiss
import numpy as np
import embedding
import json


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

    
        
    