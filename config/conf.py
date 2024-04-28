from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API configuration
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    debug: bool
    mode_prod: bool
    prod_url: str
    dev_url: str
    allowed_hosts: list
    workers: int
    prod_port: int

    # DB configuration
    database_hostname: str
    database_port: int
    database_password: str
    database_username: str

    # Celery
    celery_broker_url: str
    celery_result_backend: str
    c_force_root: bool

    class Config:
        env_file = ".env"


settings = Settings()
