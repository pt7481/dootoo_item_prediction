FROM python:3.10-slim

WORKDIR /app

RUN pip install -U pip
RUN pip install -U pipenv

COPY . .

RUN pipenv install --system --deploy

# Preload the SentenceTransformer model to ensure it is available at runtime
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]