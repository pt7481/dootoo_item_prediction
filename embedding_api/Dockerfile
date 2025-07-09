FROM python:3.10-slim

WORKDIR /app

RUN pip install -U pip
RUN pip install -U pipenv

COPY . .

RUN pipenv install --system --deploy

EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]