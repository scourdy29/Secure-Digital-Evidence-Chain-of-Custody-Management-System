from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    username: str
    password_hash: str
    role: str
    created_at: str = datetime.utcnow().isoformat()