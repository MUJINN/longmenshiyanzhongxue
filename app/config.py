from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MINERU_AUTH_TOKEN: str
    OPENROUTER_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()