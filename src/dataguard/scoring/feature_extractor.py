TOOL_FEATURES = {
    "read_dataset": 1,
    "analyze_dataset": 2,
    "external_upload": 3,
}


def extract_features(event, tool_frequency=1):

    tool = event["tool"]

    tool_id = TOOL_FEATURES.get(tool, 4)

    risk_score = event.get("risk_score", 0)

    return [
        tool_id,
        risk_score,
        tool_frequency,
    ]