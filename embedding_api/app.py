from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import uvicorn

# Initialize the model (loads a lightweight model for testing)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create FastAPI app
app = FastAPI()

# Define a request body model
class TextRequest(BaseModel):
    text: str

# Define an endpoint for getting embeddings
@app.post("/embed")
async def embed_text(request: TextRequest):
    try:
        # Get the embedding from the model
        embedding = model.encode(request.text).tolist()
        return {"embedding": embedding}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server with Uvicorn if this script is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)