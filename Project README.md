# 📘 Multi-Agent Book Writer & Editor

A fully automated multi-agent system that creates short fictional stories based on user inputs.
Users provide:
- Theme
- Characters
- Genre
- Writing style preferences

The system uses a collaborative Planner → Worker → Evaluator pipeline to create
structured, multi-chapter stories.

---

# ✨ Features

### ✔️ Planner Agent
Creates story outline, structure, character arcs, and chapter goals.

### ✔️ Worker Agent
Writes each chapter according to the outline and user preferences.

### ✔️ Evaluator Agent
Checks:
- Style
- Coherence
- Grammar
- Continuity
- Character consistency

Then applies edits or requests rewrites.

### ✔️ Memory System
Stores:
- User preferences (genre, style)
- Character details
- Previous chapter summaries
- Style guides

### ✔️ Tools
- Story outline generator
- Chapter summarizer
- Grammar checker
- Rewriting tool
- Character tracker
- A2A Protocol (agent-to-agent messaging)
- Observability logs

---

# 🧠 Multi-Agent Architecture

User Input → Planner → Worker → Evaluator → (rewrite?) → Final Chapter


Agents communicate using a structured A2A messaging protocol.

---

# 📁 Project Structure

project/
agents/
planner.py
worker.py
evaluator.py

tools/
tools.py

memory/
session_memory.py

core/
context_engineering.py
observability.py
a2a_protocol.py

main_agent.py
app.py
requirements.txt


---

# 🚀 Deployment

This project is designed for:
- Hugging Face Spaces (Gradio UI)
- Colab Notebooks
- Local Python execution

---

# 🤝 Contributing

See `CONTRIBUTING.md` for guidelines.

---

# 📄 License

This project is released under the MIT License.


