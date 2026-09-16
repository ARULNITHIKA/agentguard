AgentGuard
Runtime Trust, Observability & Risk Monitoring for AI Agents

AgentGuard is an experimental AI/ML prototype exploring how autonomous AI agents can be monitored for tool usage, data access, policy violations, risk, and unusual behaviour at runtime.

The project explores a simple question:

If an AI agent can autonomously access data and use tools, how do we know that its behaviour remains within its intended boundaries?

Why AgentGuard?

As AI systems move from generating responses to taking actions, traditional application monitoring may not be enough.

An autonomous agent can potentially:

access datasets
invoke internal or external tools
move information between systems
perform actions without direct human intervention
exhibit behavioural patterns that were not explicitly anticipated during development

AgentGuard explores whether runtime behavioural telemetry can provide an additional layer of visibility and control around such systems.

The current prototype combines deterministic policy enforcement with risk scoring, event logging, feature extraction, and initial unsupervised anomaly detection.

Architecture
                         AGENTGUARD
                              │
                              ▼
                         DATA AGENT
                              │
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
          Policy Engine   Risk Engine   Event Logger
                │             │             │
                │             │             ▼
                │             │       Runtime Events
                │             │             │
                │             └──────┐      │
                │                    ▼      │
                │             Feature       │
                │             Extraction    │
                │                    │      │
                │                    ▼      │
                │             Isolation     │
                │              Forest       │
                │                    │      │
                └─────────────┬──────┘      │
                              ▼             │
                       Agent Risk           │
                       Assessment ◄─────────┘


Current Prototype

AgentGuard currently implements five core components.

1. Policy Engine

The policy engine determines whether an agent is permitted to use a requested tool.

Example:

read_dataset       → ALLOW
analyze_dataset    → ALLOW
external_upload    → BLOCK
unknown_tool       → BLOCK

The current implementation uses an explicit allow-list and defaults unknown actions to BLOCK.

2. Risk Engine

The risk engine assigns a numerical risk score based on the requested action and data sensitivity.

Example:

read_dataset
Risk Score: 10
Level: LOW
external_upload + sensitive data
Risk Score: 80
Level: HIGH

The current scoring model is intentionally simplified and is intended for experimentation rather than production security decisions.

3. Runtime Event Monitoring

Agent actions are converted into structured runtime events.

Example:

{
  "timestamp": "2026-09-16T12:00:00",
  "agent_id": "data-agent-01",
  "event_type": "data_access",
  "tool": "read_dataset",
  "risk_level": "low",
  "risk_score": 10
}

This creates a basic behavioural telemetry layer for the agent.

4. Behavioural Feature Extraction

Runtime events are transformed into numerical features for machine-learning analysis.

The current prototype extracts features including:

tool_id
risk_score
tool_frequency

This provides the bridge between deterministic monitoring and behavioural anomaly detection.

5. Behavioural Anomaly Detection

AgentGuard uses Isolation Forest, an unsupervised machine-learning algorithm, as an initial experiment for detecting unusual behavioural patterns.

The intention is not simply to classify individual actions as "good" or "bad", but to investigate whether an agent's behavioural pattern over time can be used as a signal for runtime risk.


Example Runtime Behaviour

A simple agent interaction can produce:

Agent: data-agent-01

read_dataset
→ ALLOW
→ Risk: LOW

analyze_dataset
→ ALLOW
→ Risk: LOW

external_upload
→ BLOCK
→ Risk: MEDIUM

This demonstrates the interaction between:

Agent Action
     ↓
Policy Evaluation
     ↓
Risk Assessment
     ↓
Runtime Event
     ↓
Behavioural Features
     ↓
Anomaly Detection
Project Structure
agentguard/
│
├── examples/
│   ├── run_agent.py
│   └── test_anomaly_detector.py
│
├── src/
│   └── dataguard/
│       ├── agent/
│       │   └── agent.py
│       │
│       ├── monitoring/
│       │   └── events_logger.py
│       │
│       ├── scoring/
│       │   ├── anomaly_detector.py
│       │   ├── feature_extractor.py
│       │   └── risk_engine.py
│       │
│       └── security/
│           └── policy_engine.py
│
├── tests/
│
├── .gitignore
├── pyproject.toml
└── README.md


Research Direction

The current implementation is intentionally a prototype.

Potential directions for further investigation include:

sequence-level behavioural modelling
temporal anomaly detection
improved anomaly calibration
sensitive-data and PII signals
runtime intervention mechanisms
human-in-the-loop approval
agent identity and trust modelling
multi-agent behaviour monitoring
long-horizon behavioural analysis
evaluation datasets and benchmarks
adaptive policy enforcement

A longer-term goal would be to investigate whether policy-based controls and behavioural anomaly detection can complement each other rather than treating them as separate mechanisms.

Current Status

Prototype stage

Implemented:

Agent abstraction

Tool permission policy

Risk scoring

Runtime event logging

Behavioural feature extraction

Initial Isolation Forest integration

Example runtime scenarios


Planned:

Persistent event storage

Behavioural sequence modelling

Runtime dashboard

Improved evaluation dataset

More realistic agent scenarios

Runtime intervention experiments