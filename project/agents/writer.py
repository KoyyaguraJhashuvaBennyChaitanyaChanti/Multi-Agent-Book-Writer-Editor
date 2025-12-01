from google import genai
import os

client = genai.Client()

class WriterAgent:
    def write_chapter(self, outline, chapter_index):
        prompt = f"""
Write chapter {chapter_index+1} of the story using this outline:

{outline}

Return ONLY the chapter text.
"""

        r = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return r.text
