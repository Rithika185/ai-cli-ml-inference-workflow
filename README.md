# ML Inference API: Exam Score Predictor

This repository contains a structured local prototype for a Machine Learning inference API built with FastAPI and scikit-learn. It predicts exam scores based on hours studied using a Linear Regression model.

## 1. Project Overview
The goal of this project is to demonstrate a clean, modular approach to serving ML models. It provides a RESTful interface for real-time predictions, complete with input validation and automated testing.

## 2. Architecture
The project follows a standard modular design for Python-based ML services:
- `app/main.py`: FastAPI application, route definitions, and dependency injection.
- `app/model.py`: Model logic, including training (on-the-fly for demo) and prediction.
- `app/schemas.py`: Pydantic models for request/response validation and documentation.
- `tests/`: Automated unit tests for API endpoints and validation logic.
- `Dockerfile`: Containerization configuration for consistent deployments.

## 3. Tech Stack
- **Language:** Python 3.11
- **API Framework:** FastAPI
- **ML Framework:** scikit-learn
- **Data Handling:** NumPy
- **Validation:** Pydantic
- **Testing:** pytest & httpx
- **Containerization:** Docker

## 4. Setup Steps
### Local Development
1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the API:**
   ```bash
   uvicorn app.main:app --reload
   ```

## 5. API Endpoints
- `GET /`: Health check endpoint to verify service status.
- `POST /predict`: Submit study hours to receive a predicted score.
- `GET /docs`: Interactive Swagger UI documentation.

## 6. Example Request and Response
### Request
`POST /predict`
```json
{
  "hours_studied": 5.0
}
```

### Response
```json
{
  "predicted_score": 55.0
}
```

## 7. Testing Results
Automated tests verify endpoint availability and input validation (e.g., preventing negative hours).
- **Total Tests:** 4
- **Status:** All Passed
- **Coverage:** Health check, valid prediction, negative input validation, invalid type validation.

## 8. Docker Deployment
The application is containerized for portability and ease of deployment.
### Build
```bash
docker build -t ml-inference-api .
```
### Run
```bash
docker run -p 8000:8000 ml-inference-api
```

## 9. How AI CLI Was Used
This project was developed using **Gemini CLI**, an interactive agent that handled:
- **Research & Design:** Analyzing requirements and proposing a modular architecture.
- **Implementation:** Writing the API code, model logic, and validation schemas.
- **Testing:** Developing and executing a test suite to ensure correctness.
- **Production Review:** Identifying gaps and creating a roadmap for production readiness.
- **Dockerization:** Authoring optimized Docker configuration.

## 10. Production-Readiness Review
A comprehensive review identified the following key areas for production deployment:
- **Model Serialization:** Transition from on-the-fly training to loading pre-trained `joblib` artifacts.
- **Validation Hardening:** Adding upper bounds for inputs and global exception handling.
- **Observability:** Implementing structured logging and Prometheus metrics.
- **Security:** Running as a non-root user in Docker and adding security headers.

## 11. Future Improvements
The roadmap for scaling this service includes:
- **MLflow Integration:** Track experiments, hyperparameters, and manage model versions in a registry.
- **CI/CD Pipeline:** Automate testing, linting, and deployment to Amazon ECR using GitHub Actions.
- **Monitoring & Drift Detection:** Implement automated checks for feature and prediction drift to ensure model reliability over time.
- **AWS Deployment:** Deploy via Amazon ECS (Fargate) for scalable, serverless compute.
- **Performance:** Evaluate ONNX runtime for sub-millisecond inference latency.
