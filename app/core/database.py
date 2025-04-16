"""Módulo para la configuración y gestión de la base de datos."""

from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

# Crear el motor de base de datos SQLite
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,  # Mostrar consultas SQL en la consola (útil para desarrollo)
    connect_args={"check_same_thread": False},  # Necesario para SQLite
)


def create_db_and_tables() -> None:
    """Crea las tablas en la base de datos basadas en los modelos SQLModel."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Proporciona una sesión de base de datos.

    Yields:
        Session: Sesión de SQLModel para interactuar con la base de datos.
    """
    with Session(engine) as session:
        yield session
