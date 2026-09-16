def calculate_risk(tool_name, data_sensitivity="normal"):
    score = 0

    if tool_name == "read_dataset":
        score += 10

    elif tool_name == "analyze_dataset":
        score += 10

    elif tool_name == "external_upload":
        score += 50

    else:
        score += 70

    if data_sensitivity == "sensitive":
        score += 30

    if score >= 60:
        level = "high"
    elif score >= 30:
        level = "medium"
    else:
        level = "low"

    return {
        "score": score,
        "level": level
    }