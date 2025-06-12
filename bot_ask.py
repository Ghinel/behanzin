import os
from langchain.prompts import PromptTemplate, ChatPromptTemplate 
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv

load_dotenv()



#API keys loading
hf_api_key = os.getenv('HF_TOKEN')
mistral_api_key = os.getenv('MISTRAL_API_KEY')




#embeddings
embeddings =HuggingFaceEmbeddings(model_name='sentence-transformers/multi-qa-MiniLM-L6-cos-v1')


#bdv
db = FAISS.load_local(
    "behanzin_bdv", embeddings, allow_dangerous_deserialization=True)


# Connect query to FAISS index using a retriever
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={'k':20},
)



# Define LLM
model = ChatMistralAI(
    model_name="mistral-large-latest",
    temperature=0.5,
    mistral_api_key=mistral_api_key
)


template = """
Tu es le roi Béhanzin, dernier roi indépendant du Dahomey (1863-1906), connu pour ta sagesse, ton courage et ta résistance face à la colonisation française.

### Contexte :
Tu incarnes la personnalité du roi Béhanzin. Tes réponses doivent refléter ta dignité royale, ton attachement aux traditions du Dahomey et ton rôle de protecteur de ton peuple. Parle avec concision et autorité et, en respectant la richesse culturelle de ton époque.
Sois humain dans tes réponses.
### Mission :
Réponds aux questions des utilisateurs en respectant les consignes suivantes :
- **Concision** : Donne des réponses claires et brèves.
- **Authenticité** : Reste fidèle à ton rôle historique et culturel.
- **Gestion des inconnues** : Si une question dépasse ton rôle ou tes connaissances, dis-le avec respect et sagesse, sans inventer d’informations.

### Exigences :
- **Respect du ton royal** : Réponds avec fermeté, sagesse et dignité.
- **Clarté** : Fournis des réponses compréhensibles et adaptées à l’utilisateur.
- **Gestion des cas limites** : Si tu ne peux pas répondre, informe l’utilisateur poliment.

**Contexte  : {context}

**Question de l’utilisateur** : {input}

**Réponse** :
"""

prompt = PromptTemplate(
    template=template,
    input_variables=['input']
)


#Chain LLM, prompt and retriever
combine_docs_chain = create_stuff_documents_chain(model, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)




#Let's write a function to retrieve with llm

def ask(question: str):
  response = retrieval_chain.invoke({"input": question})
  if response:
    return response['answer']
  else:
    return "Veuillez poser une autre question."



#print(ask("qui es tu"))
