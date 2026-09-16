from sklearn.ensemble import IsolationForest


class BehaviourAnomalyDetector:

    def __init__(self):
        self.model = IsolationForest(
            contamination=0.2,
            random_state=42
        )

    def train(self, behaviour_data):
        self.model.fit(behaviour_data)

    def predict(self, behaviour_data):
        predictions = self.model.predict(behaviour_data)

        return predictions
    