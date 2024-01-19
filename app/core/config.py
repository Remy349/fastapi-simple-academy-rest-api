from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_TITLE: str = "Simple Academy REST API"
    API_VERSION: str = "v1"

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///data.db"


settings = Settings()
