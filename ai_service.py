from storage.data_store import load_logs


class AIService:

    def analyze_logs(self):
        logs = load_logs()

        if not logs:
            return []

        evidence_access_count = {}
        user_activity = {}

        for log in logs:
            evidence_id = log["evidence_id"]
            user = log["user"]

            # Count evidence access
            if evidence_id not in evidence_access_count:
                evidence_access_count[evidence_id] = 0
            evidence_access_count[evidence_id] += 1

            # Count user activity
            if user not in user_activity:
                user_activity[user] = 0
            user_activity[user] += 1

        results = []

        results.append("AI Analysis Report:")
        results.append("")

        results.append("Evidence Access Frequency:")
        for evidence_id, count in evidence_access_count.items():
            results.append(f"Evidence {evidence_id} accessed {count} times")

        results.append("")
        results.append("User Activity:")
        for user, count in user_activity.items():
            results.append(f"User {user} performed {count} actions")

        return results