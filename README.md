# AIPlanetAssignment
# 

# Med Bot

## **1. Overview**

This design doc outlines the development of a web application for a medical chatbot using chainlit. The application will utilize large language models(LLMs) that:

- Medical specific embeddings are extracted using miniLM L6 model.
- llama v2 model is used for the inferencing task.

## **2. Motivation**

- **24/7 availability:** Unlike human staff, chatbots can provide immediate assistance to website visitors at any time of day or night. This is especially valuable for urgent inquiries or for users in different time zones.
- **Personalized self-service:** Chatbots can be programmed to answer frequently asked questions (FAQs) about your services, offer symptom checkers, schedule appointments, and even provide basic medical advice. This empowers users to find the information they need quickly and easily without needing to wait for a human response.
- **Improved accessibility:** Chatbots can offer a non-intimidating way for users to access healthcare information or seek support, especially for individuals who may hesitate to contact a professional directly. This can lead to increased engagement and awareness of your services.

## **3. Success Metrics**

The medicine domain specific language is different from general language, so if the model is able to differentiate it and gives answer for the medical field then this is termed as success. For example, The term “Calculus” is related with the mathematical filed, but for the medical field it has other meaning my model is able to give answer for the medical field.

## 4. Methodology

1. **Knowledge Base Creation and Embedding:**
- The code constructs a knowledge base by loading documents from a specified directory or PDF files.
- It employs a pre-trained sentence transformer model to generate numerical embeddings for each document, representing their semantic meaning.
- These embeddings are stored within a Faiss vector database for efficient retrieval.

**2. Retrieval-Based Question Answering (QA) Model:**

- The code leverages the Langchain library to create a retrieval-based QA model.
- It utilizes a large language model (LLM) called CTransformers, specifically the Llama-2-7B-Chat-GGML model, for language understanding and text generation.
- It defines a custom prompt template to guide the LLM's response generation.

**3. Query Processing and Answer Generation:**

- When a user poses a query, the model retrieves the most relevant documents from the knowledge base using the Faiss vector store.
- It blends the retrieved information with the LLM's knowledge to formulate a comprehensive answer.
- It presents the answer to the user, along with the sources of information if available.

**4. Chatbot Integration:**

- The code incorporates the QA model into a chatbot framework using Chainlit.
- The chatbot initiates conversations, prompts users for queries, and delivers generated answers.

## 5. **Key Functionalities**

- **Document Loading:** Capabilities to load documents from PDFs and directories.
- **Embedding Generation:** Uses sentence transformers for semantic document representations.
- **Vector Store:** Employs Faiss for efficient retrieval.
- **LLM Integration:** Leverages CTransformers for language understanding and generation.
- **Custom Prompt:** Guides LLM response formulation.
- **Retrieval-Based QA:** Answers queries based on knowledge base retrieval and LLM capabilities.
- **Chatbot Interface:** Provides user-friendly interaction through Chainlit.
