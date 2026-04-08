import datetime
from storage.data_store import load_logs, save_logs


class CustodyManager:

    def log_action(self, evidence_id, user, action):
        logs = load_logs()

        log_entry = {
            "log_id": len(logs) + 1,
            "evidence_id": evidence_id,
            "user": user,
            "action": action,
            "timestamp": str(datetime.datetime.now())
        }

        logs.append(log_entry)
        save_logs(logs)

        print("Action logged.")