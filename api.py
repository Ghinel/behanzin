import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Importer la fonction ask depuis ask_bot.py
from bot_ask import ask

# Charger les variables d'environnement
load_dotenv()

hf_api_key = os.getenv('HF_TOKEN')
mistral_api_key = os.getenv('MISTRAL_API_KEY')
if not hf_api_key or not mistral_api_key:
    raise EnvironmentError("Les clés HF_TOKEN ou MISTRAL_API_KEY ne sont pas définies dans .env")

# Initialisation de FastAPI en mode debug pour afficher les erreurs
app = FastAPI(
    title="API Roi Béhanzin",
    description="Une API RAG qui répond comme le roi Béhanzin via la fonction ask",
    debug=True
)

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_endpoint(request: QueryRequest):
    try:
        # Exécuter la fonction ask
        answer = ask(request.question)
    except Exception:
        # Erreur inattendue lors du traitement
        raise HTTPException(status_code=500, detail="Oups, un problème est survenu, veuillez réessayer.")

    # Si aucun contenu renvoyé, informer l'utilisateur sans générer d'erreur 500
    if not answer:
        return {"answer": "Désolé, je n'ai pas pu formuler de réponse. Veuillez reformuler votre question."}

    return {"answer": answer}

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API du roi Béhanzin ! Utilisez POST /ask avec {'question': '...'} pour interroger."}

# Pour exécuter : 
# uvicorn api:app --reload --port 8000
