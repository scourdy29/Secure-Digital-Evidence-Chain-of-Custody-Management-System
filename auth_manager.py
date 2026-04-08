import uuid
from models.user import User
from security.passwords_util import hash_password, verify_password
from storage.data_store import load_users, save_users

class AuthManager:
    
    def register_user(self, username: str, password: str, role: str):
        users = load_users()
        
        for user in users:
            if user["username"] == username:
                print("Username already exists.")
                return None
            
        user_id = str(uuid.uuid4())
        password_hash = hash_password(password)
        
        new_user = User(id = user_id, username = username, password_hash = password_hash, role = role)
        
        users.append(new_user.__dict__)
        save_users(users)
        
        print("User registered successfully.")
        return new_user
    
    def login(self, username: str, password: str):
        users = load_users()
        
        for user in users:
            if user["username"] == username:
                if verify_password(user["password_hash"], password):
                    print("Login successful.")
                    return user
                else:
                    print("Incorrect password.")
                    return None
        
        print("User not found.")
        return None
