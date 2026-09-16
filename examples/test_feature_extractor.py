from dataguard.scoring.feature_extractor import extract_features


event = {
    "tool": "external_upload",
    "risk_score": 50
}


features = extract_features(
    event,
    tool_frequency=4
)


print("Features:", features)