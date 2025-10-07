import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    HOST: str = os.getenv("HOST")
    PORT: str = os.getenv("PORT")
    USERNAME: str = os.getenv("USERNAME")
    PASSWORD: str = os.getenv("PASSWORD")
    DATABASE: str = os.getenv("DATABASE")

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"
        )

settings = Settings()
