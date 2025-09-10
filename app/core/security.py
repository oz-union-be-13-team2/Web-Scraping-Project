from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "YPBBqW24fOr2a-jBxXFZ--giP7J1pKYsAP-Tw6rQ4PsVc8TIPDreTuXyfpf6EmJEh9SsQ0KKEAILdPR-susU7Q"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)