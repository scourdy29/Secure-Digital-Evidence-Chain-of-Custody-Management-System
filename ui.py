import tkinter as tk
from tkinter import messagebox
from services.auth_manager import AuthManager
from services.evidence_manager import EvidenceManager
from services.ai_service import AIService

evidence_manager = EvidenceManager()
ai_service = AIService()


def validate_login(username, password, frame):
    auth_manager = AuthManager()
    user = auth_manager.login(username, password)

    if user:
        messagebox.showinfo("Success", "Login successful!")
        frame.destroy()
        show_dashboard(user)
    else:
        messagebox.showerror("Error", "Invalid credentials")


def register_user(username, password):
    auth_manager = AuthManager()
    role = "Investigator"

    auth_manager.register_user(username, password, role)
    messagebox.showinfo("Success", "Registration successful!")


def show_login():
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    login_btn = tk.Button(
        frame,
        text="Login",
        command=lambda: validate_login(
            username_entry.get(),
            password_entry.get(),
            frame
        )
    )
    login_btn.grid(row=2, column=0, columnspan=2, pady=10)

    register_btn = tk.Button(
        frame,
        text="Register",
        command=lambda: register_user(
            username_entry.get(),
            password_entry.get()
        )
    )
    register_btn.grid(row=3, column=0, columnspan=2, pady=10)


def show_dashboard(user):
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text=f"Welcome, {user}!", font=("Arial", 14)).pack(pady=20)

    tk.Button(frame, 
              text="Create Evidence",
              command=lambda: create_evidence_popup(user)
              ).pack(pady=5)
    tk.Button(frame, 
              text="View Evidence",
              command=lambda: view_evidence_popup(user)
              ).pack(pady=5)
    tk.Button(frame, 
              text="AI Analysis",
              command=lambda: ai_analysis_popup()
              ).pack(pady=5)

    tk.Button(frame, text="Logout", command=lambda: logout(frame)).pack(pady=20)
    
def create_evidence_popup(user):
    popup = tk.Toplevel(root)
    popup.title("Create Evidence")
    popup.geometry("300x200")

    tk.Label(popup, text="Title").pack(pady=5)
    title_entry = tk.Entry(popup)
    title_entry.pack(pady=5)

    tk.Label(popup, text="Description").pack(pady=5)
    desc_entry = tk.Entry(popup)
    desc_entry.pack(pady=5)

    def submit():
        title = title_entry.get()
        desc = desc_entry.get()

        evidence_manager.create_evidence(title, desc, user)
        messagebox.showinfo("Success", "Evidence created!")
        popup.destroy()

    tk.Button(popup, text="Submit", command=submit).pack(pady=10)
    
def view_evidence_popup(user):
    popup = tk.Toplevel(root)
    popup.title("View Evidence")
    popup.geometry("400x300")

    evidence_list = evidence_manager.view_evidence(user)

    if not evidence_list:
        tk.Label(popup, text="No evidence found.").pack()
        return

    for ev in evidence_list:
        text = f"ID: {ev['evidence_id']} | {ev['title']} | {ev['description']}"
        tk.Label(popup, text=text).pack()

def ai_analysis_popup():
    popup = tk.Toplevel(root)
    popup.title("AI Analysis")
    popup.geometry("400x300")

    results = ai_service.analyze_logs()

    if not results:
        tk.Label(popup, text="No data available").pack(pady=10)
        return

    for line in results:
        tk.Label(popup, text=line).pack(anchor="w", padx=10, pady=2)

def logout(frame):
    frame.destroy()
    show_login()


root = tk.Tk()
root.title("Incident Response System")
root.geometry("400x300")

show_login()

root.mainloop()