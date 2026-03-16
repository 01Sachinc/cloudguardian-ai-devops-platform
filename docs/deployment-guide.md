# Deployment Guide

Follow these instructions to run the AI-Driven DevOps Automation Platform locally using Docker Compose, or provision the AWS infrastructure using Terraform.

## Prerequisites
- Docker & Docker Compose
- Terraform >= 1.0
- AWS CLI configured with appropriate permissions
- `kubectl` installed

## Local Simulation (Docker Compose)
To test the environment without deploying to AWS, use the provided Docker Compose stack.

1. **Clone Repository**
   ```bash
   git clone git@github.com:yourusername/ai-devops-automation-platform.git
   cd ai-devops-automation-platform
   ```

2. **Run Containers**
   ```bash
   docker-compose -f docker/docker-compose.yml up -d
   ```
   This spins up the application, PostgreSQL, Redis, Prometheus, and Grafana.

3. **Access Services**
   - Application: `http://localhost:3000`
   - Prometheus: `http://localhost:9090`
   - Grafana: `http://localhost:3001` (Credentials: admin / admin)

## AWS Cloud Deployment

1. **Initialize Terraform**
   ```bash
   cd terraform
   terraform init
   ```

2. **Deploy Infrastructure**
   Review the execution plan, then apply:
   ```bash
   terraform plan
   terraform apply -auto-approve
   ```
   *Note: This will provision actual AWS resources which may incur costs.*

3. **Deploy Application to EKS**
   Extract the EKS cluster setup details from Terraform outputs and configure `kubectl`:
   ```bash
   aws eks update-kubeconfig --name ai-devops-cluster --region us-east-1
   cd ../scripts
   chmod +x deploy.sh
   ./deploy.sh latest
   ```

4. **Start AI Monitoring**
   ```bash
   cd ../ai-engine
   pip install -r requirements.txt # (Assuming numpy/requests are installed)
   python incident_predictor.py
   ```
