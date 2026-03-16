# DevOps Pipeline Workflow

The automated software delivery pipeline is designed for speed, security, and reliability. 

## Flow sequence

1. **Code Commit**: Developer pushes code changes to the `main` branch.
2. **Continuous Integration**:
   - The CI server checks out the code.
   - Dependencies are installed.
   - Unit tests and static analysis tools run.
3. **Containerization**:
   - A multi-stage `Dockerfile` is utilized to build a lean production image.
   - The image is tagged with the Git commit SHA for immutability.
4. **Registry Push**:
   - The built Docker image is pushed to the Amazon Elastic Container Registry (ECR).
5. **Continuous Deployment**:
   - The pipeline retrieves the EKS cluster context.
   - Deployment manifests (`kubernetes/deployment.yaml`) are updated dynamically using `sed` to replace the placeholder image tag with the new image.
   - Manifests are applied to the Kubernetes cluster using `kubectl apply`.
6. **Post-Deployment Validation**:
   - The AI monitoring service is queried to establish a baseline for the new deployment version, watching for immediate anomalies.

---
![Pipeline Workflow](../architecture/devops-pipeline-flow.png)
