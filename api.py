from fastapi import FastAPI
from pydantic import BaseModel
from bot_ask import ask  # Import de ta fonction ask

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str




@app.post("/ask")
def ask_question(request: QuestionRequest):
    response = ask(request.question)
    return {"answer": response}

    
'''
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)'''
