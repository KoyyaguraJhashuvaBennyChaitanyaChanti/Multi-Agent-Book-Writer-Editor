import os, json, uuid

class SessionManager:
    def __init__(self, base_path="project/memory/sessions"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def new_session(self):
        sid = str(uuid.uuid4())
        path = f"{self.base_path}/{sid}.json"
        with open(path, "w") as f: json.dump({}, f)
        return sid

    def load(self, sid):
        path = f"{self.base_path}/{sid}.json"
        if not os.path.exists(path):
            with open(path, "w") as f: json.dump({}, f)
        with open(path) as f:
            return json.load(f)

    def save(self, sid, data):
        path = f"{self.base_path}/{sid}.json"
        with open(path, "w") as f: json.dump(data, f, indent=2)
