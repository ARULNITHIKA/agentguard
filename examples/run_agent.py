from dataguard.agent.agent import DataAgent


agent = DataAgent("data-agent-01")

agent.use_tool(
    "read_dataset",
    "data_access",
)

agent.use_tool(
    "analyze_dataset",
    "data_analysis",

)

agent.use_tool(
    "external_upload",
    "data_transfer",
)