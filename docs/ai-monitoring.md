# AI Monitoring & Automation

Beyond traditional threshold-based alerts, this platform includes custom Python scripts functioning as a machine learning anomaly detection engine.

## `log_analyzer.py`
Parses raw application logs looking for syntax patterns corresponding to stack traces or explicit `Error/Exception` keywords. Provides statistical frequency mapping to understand normal "background noise" vs. critical spikes.

## `anomaly_detector.py`
Uses statistical anomaly detection (Z-score evaluation) over sliding windows of time-series metric data. It learns the baseline dynamically. A sudden spike in resource usage that deviates significantly from the moving average triggers an anomaly event.

## `incident_predictor.py`
Acts as a daemon process polling the combined health of the cluster metrics and the log anomalies. If the composite score exceeds safety margins, it acts as the orchestrator to fire off external webhook alerts (e.g., to Slack, PagerDuty, or executing the `rollback.sh` script automatically).
