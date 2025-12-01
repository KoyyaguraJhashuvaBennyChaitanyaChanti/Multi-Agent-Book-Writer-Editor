from project.agents.planner import PlannerAgent
from project.agents.writer import WriterAgent
from project.agents.evaluator import EvaluatorAgent
from project.agents.character_consistency import CharacterConsistencyAgent
from project.agents.continuity_guardian import ContinuityGuardianAgent

from project.core.logger import log
from project.core.memory import LongMemory

class Coordinator:
    def __init__(self):
        self.memory = LongMemory()
        self.planner = PlannerAgent(self.memory)
        self.writer = WriterAgent()
        self.evaluator = EvaluatorAgent()
        self.char_agent = CharacterConsistencyAgent()
        self.continuity_agent = ContinuityGuardianAgent()

    def create_story(self, theme, num_chapters):
        log("Starting pipeline.")

        plan = self.planner.plan(theme, num_chapters)
        outline = plan["outline"]

        character_list = f"Characters inferred from outline: {outline}"
        self.memory.set("characters", character_list)

        story = []
        for i in range(num_chapters):
            log(f"Writing chapter {i+1}")
            ch = self.writer.write_chapter(outline, i)

            log("Evaluating chapter...")
            improved = self.evaluator.evaluate(ch)

            log("Checking character consistency...")
            consistent = self.char_agent.check(character_list, improved)

            log("Checking continuity...")
            final = self.continuity_agent.check(story, consistent)

            story.append(final)

        self.memory.set("last_story", story)
        log("Story complete.")
        return story
