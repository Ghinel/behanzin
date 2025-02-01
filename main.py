from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from poem_chat import poem
app = FastAPI()


# Modèle pour la requête
class PoemRequest(BaseModel):
    destinataire: str
    message: str
    sex_user: str
    sex_recipient: str


# Route POST pour générer un poème
@app.post("/generate-poem/")
def generate_poem(request: PoemRequest):
    try:
        result = poem(request.destinataire, request.message, request.sex_user, request.sex_recipient)
        return {"poem": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Lancer le serveur (en local)
# Commande: uvicorn nom_du_fichier:app --reload
