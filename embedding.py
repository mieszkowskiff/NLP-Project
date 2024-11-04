from langchain_openai import OpenAIEmbeddings
import numpy as np


def embedding(text: str) -> list[float]:
    """
    This function returns the embedding of the text.
    :param text: str: The text to be embedded.
    :return: dict: The embedding of the text.
    """
    return np.array(OpenAIEmbeddings(
        api_key="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"
    ).embed_query(text))

if __name__ == "__main__":
    print(embedding("Hello, World!"))