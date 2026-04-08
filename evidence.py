class Evidence:
    def __init__(self, evidence_id, title, description, created_by, timestamp):
        self.evidence_id = evidence_id
        self.title = title
        self.description = description
        self.created_by = created_by
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "evidence_id": self.evidence_id,
            "title": self.title,
            "description": self.description,
            "created_by": self.created_by,
            "timestamp": self.timestamp
        }