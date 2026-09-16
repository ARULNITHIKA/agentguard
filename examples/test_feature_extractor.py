from dataguard.scoring.feature_extractor import extract_features


event = {
    "tool": "external_upload",
    "risk_score": 10
}

features = extract_features(event)

print("Features:", features)