import os
import ollama
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough

# MultiQuery, adjusting the question, maybe future use
# from langchain.retrievers.multi_query import MultiQueryRetriever

'''
# download Ollama 3.1 (4.7 GB) on your machine
pip install langchain
pip install langchain_community
pip install langchain_core
'''

def fake_retriever(input_: dict) -> str:
    # constext
    file_name = "story1.txt"
    file_path = "../docs/" + file_name
    f = open(file_path, "r")
    return f.read()
    #return ""

llmModel = 'llama3.1:8b'
model = ChatOllama(model = llmModel)

# generate different versions of provided question to retrieve context based on
# different perspectives
# query_prompt = PromptTemplate(input_variables=["question"], template = "")

template_RAG = "Try to answer the question based on YOUR knowledge OR the context. Context: {context} Question: {question}"
prompt = ChatPromptTemplate.from_template(template_RAG)

#print(fake_retriever())

chain = (
    {"context": fake_retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)
'''
chain = (
    RunnablePassthrough.assign(question=question).assign(
        context=fake_retriever
    )
    | qa_prompt
    | llm
    | StrOutputParser()
)
'''


counter = 1
while True:
    # question
    #question = "Tell me some basic information about the sun."
    print("Dialog #" + str(counter))
    print("User: ")
    question = input() 
    if (question=="\exit"):
        break
    response = chain.invoke(question)
    print("LLAMA: " + response.content)

    with open("../ans/output.txt", "w", encoding="utf-8") as text_file:
        text_file.write("Dialog #" + str(counter) + "\n")
        text_file.write("User: " + question + "\n")
        text_file.write("LLAMA: " + response.content + "\n")
    counter += 1