from google import genai
import os

client = genai.Client()

class EvaluatorAgent:
    def evaluate(self, text):
        prompt = f"""
You are the Evaluator Agent.

Improve grammar, clarity, pacing, and emotional tone.

Fixed version:
{text}
"""

        r = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return r.text
