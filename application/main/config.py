# configs.py
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class AppConfig(BaseModel):
    """Application configurations."""

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    SETTINGS_DIR: Path = BASE_DIR.joinpath("settings")
    SETTINGS_DIR.mkdir(parents=True, exist_ok=True)

    MODELS_DIR: Path = BASE_DIR.joinpath("models")
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    ANOMALY_DETECTOR_MODEL: Path = MODELS_DIR.joinpath(
        "v1_0_0/isolation_forest_model.joblib"
    )


class GlobalConfig(BaseSettings):
    """Global configurations."""

    APP_CONFIG: AppConfig = AppConfig()

    API_NAME: Optional[str] = Field(None, env="API_NAME")
    API_DESCRIPTION: Optional[str] = Field(None, env="API_DESCRIPTION")
    API_VERSION: Optional[str] = Field(None, env="API_VERSION")
    API_DEBUG_MODE: Optional[bool] = Field(None, env="API_DEBUG_MODE")

    MONGO_HOST: Optional[str] = Field(None, env="MONGO_HOST")
    MONGO_PORT: Optional[str] = Field(None, env="MONGO_PORT")
    MONGO_USER: Optional[str] = Field(None, env="MONGO_USER")
    MONGO_PASS: Optional[str] = Field(None, env="MONGO_PASS")
    MONGO_DB: Optional[str] = Field(None, env="MONGO_DB")
    MONGO_COLLECTION: Optional[str] = Field(None, env="MONGO_COLLECTION")

    REDIS_URL: Optional[str] = Field(None, env="REDIS_URL")

    ENV: Optional[str] = Field(None, env="ENV")

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"


settings = GlobalConfig()
