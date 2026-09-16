TOOL_FEATURES = {
    "read_dataset": 1,
    "analyze_dataset": 2,
    "external_upload": 3,
}


def extract_features(event):
    tool = event["tool"]

    tool_id = TOOL_FEATURES.get(tool, 4)

    return [
        tool_id,
        event.get("risk_score", 0),
    ]