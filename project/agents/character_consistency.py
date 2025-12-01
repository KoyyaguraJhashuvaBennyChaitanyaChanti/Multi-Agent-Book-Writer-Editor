from google import genai
import os

client = genai.Client()

class CharacterConsistencyAgent:
    def check(self, character_list, chapter_text):
        prompt = f"""
You are the Character Consistency Agent.
Characters: {character_list}

Review the following chapter text for personality drift or behavior inconsistency based on the provided character list.

Chapter Text:
{chapter_text}

Return a JSON dict with two keys:
- 'consistent': true/false (indicating if character consistency is maintained)
- 'fixed_chapter': corrected chapter text (if inconsistencies were found and fixed, otherwise the original text)
"""

        r = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return r.text
