# This is the project for the Natural Language Processing course in Winter Semester 2024 - 2025, Warsaw University of Technology, MiNI

## Main aim of the project

The goal of the project is developing a model
which can serve as a specific knowledge assistant. The idea to achieve it is to implement
the Retrieval - Augmented Generation (RAG) to
already existing Large Language Model (LLM).

## Install required dependencies

```{Bash}
pip install ollama
pip install langchain
pip install langchain_community
pip install langchain_core
pip install faiss-cpu
pip install langchain_openai
pip install Wikipedia-API
pip install pandas
```

Moreover, you need to install ollama model.
As the project relies on encoding provided by OpenAI api, it is required to create own API key on [this link](https://platform.openai.com/api-keys) and paste it in the file /source_code/embedding.py on line 7.
