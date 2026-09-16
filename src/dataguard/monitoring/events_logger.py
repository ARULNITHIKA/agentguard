from datetime import datetime


def log_event(agent_id, event_type, tool, risk_level="low"):
    event = {
        "timestamp": datetime.now().isoformat(),
        "agent_id": agent_id,
        "event_type": event_type,
        "tool": tool,
        "risk_level": risk_level,
    }

    return event