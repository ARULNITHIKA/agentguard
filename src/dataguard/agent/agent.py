from dataguard.monitoring.events_logger import log_event
from dataguard.security.policy_engine import check_tool_permission
from dataguard.scoring.risk_engine import calculate_risk
class DataAgent:

    def __init__(self, agent_id):
        self.agent_id = agent_id

    def use_tool(self, tool_name, event_type, data_sensitivity="normal"):
        permission = check_tool_permission(tool_name)
        risk=calculate_risk(tool_name, data_sensitivity)
        if permission == "BLOCK":
            print(
                f"[BLOCKED] Agent '{self.agent_id}' "
                f"attempted to use '{tool_name}'"
                f'(risk: {risk["score"]}, level: {risk["level"]})'
            )
            return None

        event = log_event(
            self.agent_id,
            event_type,
            tool_name,
            risk["level"]
        )

        print(event)

        return event