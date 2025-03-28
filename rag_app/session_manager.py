# session_manager.py
class SessionManager:
    def __init__(self):
        self.sessions = {}

    def get_history(self, session_id):
        return self.sessions.get(session_id, [])

    def add_to_history(self, session_id, prompt):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append(prompt)
        if len(self.sessions[session_id]) > 5:
            self.sessions[session_id].pop(0)