import datetime
import hashlib

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Class that initializes env variables"""

    PUBLIC_KEY: str
    PRIVATE_KEY: str
    API_URL: str

    def create_ts_and_hash(self):
        """Create hash of timestamp + private key + public key"""

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        hash_md5 = hashlib.md5(
            f"{timestamp}{self.PRIVATE_KEY}{self.PUBLIC_KEY}".encode("utf-8")
        )
        hashed_params = hash_md5.hexdigest()

        return timestamp, hashed_params

    class Config:
        """Set env file"""

        env_file = ".env"
