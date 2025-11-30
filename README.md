flowchart TD

UI(Gradio UI\napp.py) --> COORD(Coordinator.py)

COORD --> P(PlannerAgent\nCinematic Outline)
COORD --> W(WriterAgent\nStory Chapters)
COORD --> E(EvaluatorAgent\nScore + Rewrite)
COORD --> CC(CharacterConsistency\nTraits Fix)
COORD --> CG(ContinuityGuardian\nTimeline Fix)

COORD --> MEM(LongMemory\noutline + characters + stories)
COORD --> LOG(Logger)

subgraph Automation["GitHub Automation"]
    DAILY(Daily Story Generator\nrun_daily.py)
    WORKFLOW(.github/workflows/daily_stories.yml)
end

DAILY --> MEM
WORKFLOW --> DAILY
