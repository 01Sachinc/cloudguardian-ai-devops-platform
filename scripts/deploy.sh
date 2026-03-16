#!/bin/bash
set -e

echo "Starting deployment process..."

# Enforce cluster context availability
kubectl cluster-info || { echo "Kubernetes cluster not reachable"; exit 1; }

# Update image tag
export IMAGE_TAG=${1:-latest}
echo "Deploying image with tag: $IMAGE_TAG"

# Apply definitions
kubectl apply -f ../kubernetes/deployment.yaml
kubectl apply -f ../kubernetes/service.yaml
kubectl apply -f ../kubernetes/ingress.yaml

# Rollout status
kubectl rollout status deployment/ai-devops-app

echo "Deployment completed successfully. App is running."
