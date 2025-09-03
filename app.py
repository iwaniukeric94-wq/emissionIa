  from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import spacy

app = FastAPI()

# Configurer CORS pour permettre les requêtes depuis le client JavaScript
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Charger le modèle français de SpaCy
nlp = spacy.load("fr_core_news_sm")

@app.post("/analyze")
async def analyze_text(data: dict):
	text = data.get("text", "")
	doc = nlp(text)
	results = [{"word": t.text, "pos": t.pos_, "lemma": t.lemma_} for t in doc]
	return {"results": results}
