ALLOWED_TOOLS = {
    "read_dataset",
    "analyze_dataset",
}


def check_tool_permission(tool_name):
    if tool_name in ALLOWED_TOOLS:
        return "ALLOW"

    return "BLOCK"