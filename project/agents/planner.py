from google import genai
import os
import json

client = genai.Client()

class PlannerAgent:
    def __init__(self, memory):
        self.memory = memory

    def plan(self, theme, num_chapters):
        if "outline" in self.memory.data:
            return {"source": "memory", "outline": self.memory.data["outline"]}

        prompt = f"""
You are the Planner Agent.

User theme: {theme}
Number of chapters: {num_chapters}

Create a structured chapter outline in JSON.
If memory is empty, state:
'I am providing this outline from LLM because agents have no memory.'
"""

        r = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        outline = r.text
        self.memory.set("outline", outline)

        return {"source": "llm", "outline": outline}
