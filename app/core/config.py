"""Módulo de configuración para la aplicación."""


from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración de la aplicación.

    Attributes:
        API_V1_STR: Prefijo para las rutas de la API v1.
        PROJECT_NAME: Nombre del proyecto.
        DATABASE_URL: URL de conexión a la base de datos.
    """

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Tienda API"
    DATABASE_URL: str = "sqlite:///./sql_app.db"

    class Config:
        """Configuración de la clase Settings."""

        env_file = ".env"
        case_sensitive = True


settings = Settings()
