# Quora Question Pair Duplicate Detection

A Machine Learning and NLP-powered web application that predicts whether two Quora questions are duplicates or not. The project combines advanced text preprocessing, handcrafted similarity features, Bag-of-Words vectorization, and an XGBoost classifier, exposed through a FastAPI backend and an interactive Streamlit frontend.

---

## Project Overview

Duplicate questions are common on community-driven platforms such as Quora. Identifying semantically similar questions helps:

- Reduce duplicate content
- Improve search quality
- Enhance user experience
- Optimize knowledge organization

This project predicts whether two questions convey the same intent.

---

## Features

- Text preprocessing and normalization
- Contraction handling
- HTML tag removal
- Stopword-based similarity analysis
- Fuzzy string matching features
- Longest common substring similarity
- Bag-of-Words vectorization
- XGBoost classification model
- FastAPI REST API
- Streamlit user interface
- Pydantic request validation
- Logging support
- Docker containerization
- Pytest unit testing

---

## Tech Stack

### Machine Learning & NLP

- Python
- Scikit-Learn
- XGBoost
- NLTK
- BeautifulSoup
- FuzzyWuzzy
- Distance

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Frontend

- Streamlit

### Deployment & Testing

- Docker
- Pytest

---

## Project Structure

```text
quora_duplicate_detection/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── logger.py
│   │   └── config.py
│   │
│   ├── schemas/
│   │   └── prediction_schema.py
│   │
│   ├── services/
│   │   └── prediction_service.py
│   │
│   ├── utils/
│   │   └── text_preprocessing.py
│   │
│   └── main.py
│
├── models/
│   ├── xgboost_classifier.pkl
│   └── vectorizer.pkl
│
├── streamlit_app/
│   └── app.py
│
├── tests/
│   ├── test_api.py
│   └── test_prediction.py
│
├── logs/
│   └── app.log
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Machine Learning Pipeline

### 1. Text Preprocessing

- Lowercasing
- Contraction expansion
- Special character replacement
- HTML removal
- Punctuation removal

### 2. Feature Engineering

#### Token Features

- Common word ratio
- Common stopword ratio
- Common token ratio
- First word match
- Last word match

#### Length Features

- Absolute length difference
- Mean length
- Longest common substring ratio

#### Fuzzy Matching Features

- Fuzz Ratio
- Partial Ratio
- Token Sort Ratio
- Token Set Ratio

### 3. Vectorization

Bag-of-Words Vectorization using Scikit-Learn.

### 4. Classification

XGBoost Classifier

---

## API Endpoint

### Health Check

```http
GET /
```

Response

```json
{
  "message": "API Running Successfully"
}
```

---

### Prediction Endpoint

```http
POST /predict
```

Request Body

```json
{
  "question1": "How can I learn Python?",
  "question2": "What is the best way to learn Python?"
}
```

Response

```json
{
  "prediction": "Duplicate",
  "confidence": 0.95
}
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/quora-duplicate-detection.git

cd quora-duplicate-detection
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Linux/Mac

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Streamlit

```bash
streamlit run streamlit_app/app.py
```

Application URL:

```text
http://localhost:8501
```

---

## Running Tests

```bash
pytest
```

---

## Docker Setup

### Build Image

```bash
docker build -t quora-duplicate .
```

### Run Container

```bash
docker run -p 8000:8000 quora-duplicate
```


## Future Improvements

- TF-IDF Vectorization
- Sentence Transformers Embeddings
- BERT-based Similarity Detection
- CI/CD Pipeline
- Cloud Deployment
- MLflow Integration
- Model Monitoring



## Author

**Sangita Bera**

GitHub: https://github.com/sangitabera



## License

This project is licensed under the MIT License.