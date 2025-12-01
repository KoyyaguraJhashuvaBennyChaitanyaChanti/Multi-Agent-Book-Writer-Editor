import json
import os

class LongMemory:
    def __init__(self, path="project/memory/memory.json"):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w") as f: json.dump({}, f)
        with open(self.path) as f:
            self.data = json.load(f)

    def set(self, key, value):
        self.data[key] = value
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def get(self, key):
        return self.data.get(key)
