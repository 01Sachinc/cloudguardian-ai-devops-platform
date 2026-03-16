#!/bin/bash
set -e

echo "Initiating rollback procedure..."

# Undo the last deployment
kubectl rollout undo deployment/ai-devops-app

# Monitor the rollback status
kubectl rollout status deployment/ai-devops-app

echo "Rollback completed successfully. Reverted to previous stable version."
