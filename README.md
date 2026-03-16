# AI-Driven DevOps Automation Platform

![GitHub Action Status](https://img.shields.io/badge/build-passing-brightgreen)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=flat&logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)

An enterprise-grade DevOps portfolio project demonstrating a complete cloud-native deployment lifecycle integrated with real-time AI-powered monitoring and automated incident remediation.

---

## 📖 Project Overview

This repository is designed to showcase mastery over modern software delivery pipelines and infrastructure management. It simulates a highly available web application deployed to AWS Elastic Kubernetes Service (EKS) via Terraform. 

**Key Objectives:**
- Provide **Infrastructure as Code (IaC)** templates for reproducible cloud environments.
- Enforce **Continuous Integration & Continuous Deployment (CI/CD)** automating the path from commit to production.
- Implement **Centralized Observability** using Prometheus and Grafana.
- Introduce an **AI Monitoring Engine** evaluating log streams and metric anomalies to predict catastrophic failures before they cascade.

## 🛠️ Technology Stack

| Category         | Technologies Used                                     |
|------------------|-------------------------------------------------------|
| **DevOps Tools** | Docker, Kubernetes, Terraform, Helm, Git              |
| **CI/CD**        | GitHub Actions, Jenkins                               |
| **Monitoring**   | Prometheus, Grafana, ELK Stack (simulated outputs)    |
| **Scripting & AI**| Bash, Python (NumPy, custom anomaly detection models) |
| **Cloud (AWS)**  | VPC, EKS, EC2, ECR, IAM, S3, CloudWatch               |

---

## 🏛️ System Architecture diagram

The application follows a stateless microservice architecture decoupled from its stateful data stores (PostgreSQL / Redis), scaling dynamically within Kubernetes. 

![System Architecture](architecture/system-architecture.png)

_For a deep dive, read the [Architecture Overview](docs/architecture-overview.md)._

## 🚀 DevOps Pipeline Flow

1. **Commit:** Developer pushes code to the repository.
2. **Build:** GitHub Actions runs automated tests and linters.
3. **Containerize:** Docker builds the image and pushes to Amazon ECR.
4. **Provision:** Terraform ensures the AWS infrastructure (VPC, EKS) is at the desired state.
5. **Deploy:** Kubernetes applies the manifest updates performing a zero-downtime rolling update.
6. **Observe:** Metric endpoints are scraped by Prometheus, feeding into Grafana dashboards.
7. **Analyze:** AI-Engine validates system stability post-deployment.

![DevOps Pipeline](architecture/devops-pipeline-flow.png)

_For details, see the [Pipeline Workflow Documentation](docs/pipeline-workflow.md)._

## 👁️ Monitoring Architecture

Prometheus is configured with sophisticated Service Discovery targeting Kubernetes nodes and application Endpoints. Grafana connects to Prometheus, exposing the following golden signals:
- **Latency / Response Time**
- **Traffic Volume**
- **Error Rates**
- **Saturation (CPU / Memory)**

![Monitoring Dashboard](architecture/monitoring-architecture.png)

_Learn more in the [Monitoring System Guide](docs/monitoring-system.md)._

---

## 🧠 AI Monitoring Module

Unlike static alert systems mapped to manual thresholds, this platform deploys Python-based ML heuristic models.

1. **`log_analyzer.py`**: Scans application logs to build frequency mappings of error patterns.
2. **`anomaly_detector.py`**: Continuously calculates Z-Scores of resource consumption, triggering alerts if a metric massively deviates from the moving average.
3. **`incident_predictor.py`**: Coordinates anomalies across metrics and logs to fire actionable warnings (e.g., PagerDuty webhooks, auto-rollback).

_See [AI Monitoring Strategy](docs/ai-monitoring.md) for specifics._

---

## 📂 Project Structure

```text
ai-devops-automation-platform/
├── README.md                          # Repository overview (this file)
├── architecture/                      # Architectural diagrams and screenshots
├── terraform/                         # IaC for AWS VPC, Networking, EKS
├── docker/                            # Multi-stage Dockerfile and local docker-compose
├── kubernetes/                        # K8s manifest files (Deployment, Service, Ingress)
├── ci-cd/                             # GitHub Actions & Jenkins pipelines
├── scripts/                           # Bash deployment and rollback automation
├── monitoring/                        # Prometheus targets & Grafana Dashboards
├── ai-engine/                         # Python anomaly detection & log analysis code
└── docs/                              # Comprehensive technical documentation
```

---

## 🏁 Deployment Instructions

To spin up this project, see the full [Deployment Guide](docs/deployment-guide.md). A quick-start simulation is available using Docker Compose:

1. **Clone the repository:**
   ```bash
   git clone git@github.com:yourusername/ai-devops-automation-platform.git
   cd ai-devops-automation-platform
   ```

2. **Launch the local stack:**
   ```bash
   docker-compose -f docker/docker-compose.yml up -d
   ```

3. **Validate:**
   - Web App: `http://localhost:3000`
   - Grafana Dashboard: `http://localhost:3001`
   - Prometheus: `http://localhost:9090`

---

## 📸 Screenshots & Proof of Work

### Docker Container Running
![Docker Status](architecture/system-architecture.png)

### CI/CD Pipeline Execution
![GitHub Actions](architecture/devops-pipeline-flow.png)

### Kubernetes Pods Status
```text
NAME                                 READY   STATUS    RESTARTS   AGE
ai-devops-app-79c8849b7-abc12        1/1     Running   0          5m
ai-devops-app-79c8849b7-def34        1/1     Running   0          5m
```

### AI Anomaly Detection Output
```text
2023-11-01 10:14:22 - AnomalyDetector - WARNING - Anomaly detected! Value: 95.0, Z-Score: 3.12
ALERT: High probability of crash: CPU and error rates are elevated.
```

---
*Created by a DevOps Engineer. Not designed for production use without securing credentials.*
