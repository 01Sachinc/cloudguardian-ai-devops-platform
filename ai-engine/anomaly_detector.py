import numpy as np
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AnomalyDetector")

class AnomalyDetector:
    def __init__(self, threshold=3.0):
        self.threshold = threshold
        self.historical_data = []

    def feed_data(self, data_point):
        self.historical_data.append(data_point)
        # Keep window size manageable
        if len(self.historical_data) > 1000:
            self.historical_data.pop(0)

    def detect(self, current_value):
        if len(self.historical_data) < 10:
            return False, 0.0

        mean = np.mean(self.historical_data)
        std_dev = np.std(self.historical_data)

        if std_dev == 0:
            return False, 0.0

        z_score = abs((current_value - mean) / std_dev)
        is_anomaly = z_score > self.threshold
        
        if is_anomaly:
            logger.warning(f"Anomaly detected! Value: {current_value}, Z-Score: {z_score:.2f}")

        return is_anomaly, z_score

if __name__ == "__main__":
    detector = AnomalyDetector(threshold=2.5)
    
    # Simulate data
    print("Simulating metrics stream...")
    for _ in range(50):
        val = random.normalvariate(50, 5) # Normal metrics
        detector.feed_data(val)
        
    # Inject anomaly
    anomaly_val = 95.0
    print(f"Injecting anomaly metric: {anomaly_val}")
    is_anomaly, score = detector.detect(anomaly_val)
    print(f"Anomaly result: {is_anomaly} (Score: {score:.2f})")
