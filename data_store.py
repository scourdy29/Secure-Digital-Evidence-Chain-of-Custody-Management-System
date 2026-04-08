import json
from pathlib import Path 

DATA_DIR = Path("data")
USERS_FILE = DATA_DIR / "users.json"

# User functions
def load_users():
    if not USERS_FILE.exists():
        return []
    
    with open(USERS_FILE, "r") as f:
        return json.load(f)
    
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent = 4)
        

# Evidence Functions 
EVIDENCE_FILE = DATA_DIR / "evidence.json"


def load_evidence():
    if not EVIDENCE_FILE.exists():
        return []
    
    with open(EVIDENCE_FILE, "r") as f:
        return json.load(f)


def save_evidence(evidence):
    with open(EVIDENCE_FILE, "w") as f:
        json.dump(evidence, f, indent=4)
        
# Log Functions
LOGS_FILE = DATA_DIR / "logs.json"

def load_logs():
    if not LOGS_FILE.exists():
        return []
    
    with open(LOGS_FILE, "r") as f:
        return json.load(f)


def save_logs(logs):
    with open(LOGS_FILE, "w") as f:
        json.dump(logs, f, indent=4)