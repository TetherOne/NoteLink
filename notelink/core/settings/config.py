from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class APIPrefix(BaseModel):
    prefix: str = "/api"
    version: str = "/v1"
    notes: str = "/notes"

    @property
    def full_prefix(self) -> str:
        return f"{self.prefix}{self.version}"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="envs/.main-env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FAST_API_HH__",
        arbitrary_types_allowed=True,
    )
    api: APIPrefix = APIPrefix()
    db: DatabaseConfig


settings = Settings()
