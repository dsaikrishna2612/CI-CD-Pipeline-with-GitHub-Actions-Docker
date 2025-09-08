# CI-CD-Pipeline-with-GitHub-Actions-Docker

## 📌 Overview
This project demonstrates a complete CI/CD pipeline using GitHub Actions to build, test, and deploy a containerized Python web application.

## 🚀 Features
- GitHub Actions workflow for CI/CD
- Docker containerization
- Local deployment using Minikube
- Automated testing with Pytest

## 🛠️ Setup Instructions
1. Clone the repository
2. Build Docker image:
   ```bash
   docker build -t myapp .
3. Run tests:
   pytest tests/
4. Push to Docker Hub (configure secrets in GitHub)
5. minikube start
   kubectl apply -f deployment.yaml



📂 Folder Structure

app/: Source code and tests

.github/workflows/: CI/CD pipeline config

deployment_screenshots/: Visual proof of deployment
