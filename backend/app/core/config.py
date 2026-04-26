import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
settings = Settings()
