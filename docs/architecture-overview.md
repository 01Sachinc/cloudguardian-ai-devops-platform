# System Architecture Overview

This project embodies a state-of-the-art **AI-Driven DevOps Automation Platform**, mimicking a real enterprise-scale deployment.

## Key Components

1. **Infrastructure Platform**
   - Cloud Provider: AWS
   - Orchestration: Amazon EKS (Elastic Kubernetes Service)
   - Provisioning: Terraform
   - The platform relies on a highly available Virtual Private Cloud (VPC) with spanning public and private subnets, ensuring security for internal services while enabling internet access via gateways.

2. **Application Layer**
   - Containerized microservices pattern using Docker.
   - Designed for stateless operation (e.g., Node.js backend) to scale horizontally inside Kubernetes.
   - Stateful services (e.g., PostgreSQL, Redis) configured for persistent volume claims in real-world scenarios.

3. **CI/CD Pipeline**
   - Code is hosted on GitHub.
   - **GitHub Actions** handles continuous integration: running tests, linting, building Docker images, and pushing to Amazon ECR.
   - Continuous Deployment directly to EKS configurations.

4. **Monitoring & AI Layer**
   - **Prometheus**: Aggregates metrics from the cluster and applications.
   - **Grafana**: Visualizes system health via unified dashboards.
   - **AI Engine**: Python-based log analysis and anomaly detection stream metrics to predict incidents before they impact users.

---
```mermaid
graph TD
    subgraph "Cloud Strategy"
        Provision[Terraform IaC] --> VPC[AWS Virtual Private Cloud]
        VPC --> Subnets[Public & Private Subnets]
    end

    subgraph "Compute & Scaling"
        EKS[Amazon EKS Cluster]
        EKS --> Nodes[Managed Node Groups]
        Nodes --> Pods[Application Microservices]
    end

    subgraph "Security"
        IAM[IAM Roles for Service Accounts]
        Secrets[K8s Secrets Management]
    end

    VPC --> EKS
```
