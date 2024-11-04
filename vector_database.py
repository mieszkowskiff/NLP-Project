from langchain_chroma import Chroma
import numpy as np



def load(path: str = "chroma_db") -> Chroma:
    db = Chroma(persist_directory = path)
    return db
    