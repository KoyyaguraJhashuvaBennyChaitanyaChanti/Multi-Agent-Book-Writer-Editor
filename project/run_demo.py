from project.core.coordinator import Coordinator

if __name__ == "__main__":
    c = Coordinator()
    story = c.create_story("A misty mountain guarded by shadows", 2)
    print("\n\n".join(story))
