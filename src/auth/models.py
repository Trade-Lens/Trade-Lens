from passlib.hash import pbkdf2_sha256 as sha256

class UserModel:
    @staticmethod
    def hash_password(password: str) -> str:
        return sha256.hash(password)

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        return sha256.verify(password, hashed)
