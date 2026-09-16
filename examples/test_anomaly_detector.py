from dataguard.scoring.anomaly_detector import BehaviourAnomalyDetector


detector = BehaviourAnomalyDetector()


normal_behaviour = [
    [1, 1],
    [1, 1],
    [1, 2],
    [2, 1],
    [2, 2],
    [1, 2],
    [2, 2],
    [1, 1],
]


suspicious_behaviour = [
    [10, 10],
    [10, 10],
]


detector.train(normal_behaviour)

result = detector.predict(suspicious_behaviour)

print("Prediction:", result)