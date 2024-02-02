from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
