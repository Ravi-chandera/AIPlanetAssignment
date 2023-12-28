from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl

DB_FAISS_PATH = 'vectorstore/db_faiss'

custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt


#Loading the model
def load_llm():
    # Load the locally downloaded model here
    llm = CTransformers(
        model = "TheBloke/CodeLlama-34B-Instruct-GGUF",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

#QA Model Function
def qa_bot():

  embeddings = HuggingFaceEmbeddings(
     model_name="sentence-transformers/all-MiniLM-L6-v2",
     model_kwargs={'device': 'cuda'}
  )
  
  llm = load_llm()
  qa_prompt = set_custom_prompt()
  
  return llm, qa_prompt

#output function
def final_result(query, llm, prompt):
  
  response = llm(prompt.format(question=query))
  return response
    

#chainlit code
@cl.on_chat_start
async def start():
  llm, prompt = qa_bot()
  
  msg = cl.Message(content="Starting...")
  await msg.send()  

@cl.on_message
async def main(message: cl.Message):

  llm, prompt = cl.user_session.get("bot")
  
  answer = final_result(message.content, llm, prompt)
  
  await cl.Message(content=answer).send()
