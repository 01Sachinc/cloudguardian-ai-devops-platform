import time
import requests

def fetch_metrics():
    # Placeholder for fetching Prometheus metrics
    return {"cpu_usage": 0.65, "error_rate": 0.02}

def predict_incident(metrics):
    if metrics["cpu_usage"] > 0.85 and metrics["error_rate"] > 0.05:
        return True, "High probability of crash: CPU and error rates are elevated."
    elif metrics["error_rate"] > 0.1:
        return True, "Critical error rate spike detected."
    return False, "System stable."

def run_predictor_daemon():
    print("Starting AI incident predictor daemon...")
    while True:
        metrics = fetch_metrics()
        incident_predicted, reason = predict_incident(metrics)
        if incident_predicted:
            # Code to trigger PagerDuty or an alert webhook goes here
            print(f"ALERT: {reason}")
        time.sleep(60)

if __name__ == "__main__":
    run_predictor_daemon()
