import datetime
from models.evidence import Evidence
from storage.data_store import load_evidence, save_evidence
from services.custody_manager import CustodyManager


class EvidenceManager:

    def create_evidence(self, title, description, user):
        evidence_list = load_evidence()

        evidence_id = len(evidence_list) + 1

        evidence = Evidence(
            evidence_id,
            title,
            description,
            user,
            str(datetime.datetime.now())
        )

        evidence_list.append(evidence.to_dict())
        save_evidence(evidence_list)

        print("Evidence created successfully.")

        # Log creation (Chain of Custody)
        custody_manager = CustodyManager()
        custody_manager.log_action(
            evidence_id,
            user,
            "Created Evidence"
        )


    def view_evidence(self, user):
        evidence_list = load_evidence()

        if not evidence_list:
            print("No evidence found.")
            return

        print("\n--- Evidence List ---")

        custody_manager = CustodyManager()  # create once

        for ev in evidence_list:
            print(f"ID: {ev['evidence_id']}")
            print(f"Title: {ev['title']}")
            print(f"Description: {ev['description']}")
            print(f"Created By: {ev['created_by']}")
            print(f"Timestamp: {ev['timestamp']}")
            print("----------------------")

            # Log viewing
            custody_manager.log_action(
                ev["evidence_id"],
                user,
                "Viewed Evidence"
            )
            
            return evidence_list    