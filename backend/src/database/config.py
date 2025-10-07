import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_USERNAME: str = os.getenv("DB_USERNAME", 'postgres')
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST", 'localhost')
    DB_PORT: str = os.getenv("DB_PORT", '5432')
    DB_NAME: str = os.getenv("DB_DATABASE", 'bankdb')

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()
