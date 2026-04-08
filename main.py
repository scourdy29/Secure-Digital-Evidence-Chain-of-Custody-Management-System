from services.auth_manager import AuthManager
from services.evidence_manager import EvidenceManager
from services.ai_service import AIService

auth = AuthManager()
evidence_manager = EvidenceManager()
ai_service = AIService()


def evidence_menu(username):
    while True:
        print("\nEvidence Menu")
        print("1. Create Evidence")
        print("2. View Evidence")
        print("3. AI Analysis")
        print("4. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter evidence title: ")
            description = input("Enter evidence description: ")

            evidence_manager.create_evidence(title, description, username)

        elif choice == "2":
            evidence_manager.view_evidence(username)

        elif choice == "3":
            ai_service.analyze_logs()
            
        elif choice == "4":
            break

        else:
            print("Invalid option.")


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role (Investigator/Technician/Auditor): ")
        auth.register_user(username, password, role)

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")

        user = auth.login(username, password)

        if user:
            evidence_menu(username)

    elif choice == "3":
        break