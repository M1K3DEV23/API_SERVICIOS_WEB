"""Punto de entrada principal para la API REST."""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.core.config import settings
from app.core.database import create_db_and_tables
from app.modules.figuras_coleccion.routes import router as figuras_coleccion_router
from app.modules.joyeria.routes import router as joyeria_router
from app.modules.productos.routes import router as productos_router
from app.modules.videojuegos.routes import router as videojuegos_router


def lifespan(app: FastAPI):
    """Ejecuta acciones al iniciar la aplicación."""
    print("Iniciando la aplicación...")
    create_db_and_tables()
    print("Base de datos y tablas creadas.")
    yield
    print("Cerrando la aplicación...")
    # Aquí puedes agregar acciones de limpieza, como cerrar conexiones a bases de datos, etc.


# Crear la aplicación FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(
    productos_router, prefix=f"{settings.API_V1_STR}/productos", tags=["productos"]
)
app.include_router(
    videojuegos_router,
    prefix=f"{settings.API_V1_STR}/videojuegos",
    tags=["videojuegos"],
)
app.include_router(
    figuras_coleccion_router,
    prefix=f"{settings.API_V1_STR}/figuras-coleccion",
    tags=["figuras_coleccion"],
)
app.include_router(
    joyeria_router,
    prefix=f"{settings.API_V1_STR}/joyeria",
    tags=["joyeria"],
)


# Personalizar la documentación OpenAPI
def custom_openapi():
    """Personaliza la documentación OpenAPI."""
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=f"{settings.PROJECT_NAME} API",
        version="1.0.0",
        description="API REST para gestionar productos, videojuegos, figuras de colección y joyería de una tienda",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
def root():
    """Ruta raíz de la API."""
    return {
        "message": "Bienvenido a la API de Productos, Videojuegos, Figuras de Colección y Joyería",
        "docs": "/docs",
        "redoc": "/redoc",
    }


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
