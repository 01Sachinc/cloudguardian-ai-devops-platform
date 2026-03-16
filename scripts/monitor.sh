#!/bin/bash

echo "Starting monitoring baseline checks..."

# Check cluster nodes
echo "Node Status:"
kubectl get nodes

# Check pod health
echo "Pod Health:"
kubectl get pods --field-selector=status.phase!=Running | grep -v "No resources found" || echo "All pods running."

# Forward Prometheus port to check metrics if running locally
echo "Metrics endpoint available at http://localhost:9090"
