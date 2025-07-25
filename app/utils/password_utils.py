import os
import base64
from argon2 import PasswordHasher, exceptions

ph = PasswordHasher(
    time_cost=3,  # number of iterations
    memory_cost=64 * 1024,  # 64 MiB
    parallelism=4,  # how many threads to use
    hash_len=32,  # length of the derived key
    salt_len=16,  # length of random salt
)


class PasswordUtils:
    @staticmethod
    def hash_password(plain_password: str, salt: str) -> str:
        argon2_hash = ph.hash(
            salt + plain_password + (os.environ.get("PEPPER") or "black_pepper")
        ).encode("utf-8")

        return base64.b64encode(argon2_hash.encode("utf-8")).decode("utf-8")

    @staticmethod
    def verify_password(stored_hash_b64: str, attempt_password: str, salt: str) -> bool:
        try:
            stored_hash = base64.b64decode(stored_hash_b64).decode("utf-8")
        except Exception:
            return False

        try:
            ph.verify(
                stored_hash,
                (
                    salt
                    + attempt_password
                    + (os.environ.get("PEPPER") or "black_pepper")
                ),
            ).encode("utf-8")

            return True
        except exceptions.VerifyMismatchError:
            return False
        except Exception:
            return False
