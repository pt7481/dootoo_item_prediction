#!/bin/bash

# Comments start with #
echo "Starting MLflow UI..."

# Navigate to your project directory
cd /home/pt7481/dev/dootoo_item_prediction/eda

# Activate pipenv environment and start MLflow
pipenv run mlflow ui --backend-store-uri sqlite:///mlflow.db --host 0.0.0.0 --port 5000

echo "MLflow UI started at http://localhost:5000"
