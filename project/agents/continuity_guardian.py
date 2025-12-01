from google import genai
import os

client = genai.Client()

class ContinuityGuardianAgent:
    def check(self, previous_chapters, current_chapter):
        # Convert previous_chapters list to a readable string for the prompt
        previous_chapters_str = "\n".join([f"Chapter {i+1}:\n{ch}" for i, ch in enumerate(previous_chapters)])
        if not previous_chapters_str:
            previous_chapters_str = "No previous chapters available."

        prompt = f"""
You are the Continuity Guardian Agent.

Review the current chapter against the provided previous chapters. Look for contradictions, plot holes, timeline errors, or any inconsistencies.

Previous Chapters:
{previous_chapters_str}

Current Chapter to Review:
{current_chapter}

Return JSON with two keys:
- 'issues': a list of any identified issues (each item should be a dict with 'type', 'description', 'location' keys).
- 'fixed_chapter': the corrected chapter text, with any identified issues resolved. If no issues, return the original current_chapter text.
"""

        r = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return r.text
