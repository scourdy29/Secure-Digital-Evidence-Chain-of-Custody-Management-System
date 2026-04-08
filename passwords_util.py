import hashlib
import secrets

def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    pwd_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}${pwd_hash}"

def verify_password(stored_password: str, provided_password: str) -> bool:
    salt, pwd_hash = stored_password.split('$')
    check_hash = hashlib.sha256((salt + provided_password).encode()).hexdigest()
    return check_hash == pwd_hash

