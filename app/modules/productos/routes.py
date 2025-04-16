"""Módulo que define las rutas de la API para productos."""

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session

from app.core.database import get_session
from app.modules.productos.crud import (
    create_producto,
    delete_producto,
    get_producto,
    get_productos,
    update_producto,
)
from app.modules.productos.models import (
    ProductoCreate,
    ProductoRead,
    ProductoUpdate,
)

router = APIRouter()


@router.post("/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED)
def create_producto_route(
    producto: ProductoCreate, db: Session = Depends(get_session)
) -> Any:
    """Crea un nuevo producto.

    Args:
        producto: Datos del producto a crear.
        db: Sesión de base de datos.

    Returns:
        ProductoRead: El producto creado.
    """
    return create_producto(db=db, producto=producto)


@router.get("/{producto_id}", response_model=ProductoRead)
def read_producto(producto_id: int, db: Session = Depends(get_session)) -> Any:
    """Obtiene un producto por su ID.

    Args:
        producto_id: ID del producto a buscar.
        db: Sesión de base de datos.

    Returns:
        ProductoRead: El producto encontrado.
    """
    return get_producto(db=db, producto_id=producto_id)


@router.get("/", response_model=List[ProductoRead])
def read_productos(
    db: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
    categoria: Optional[str] = Query(None, description="Filtrar por categoría"),
) -> Any:
    """Obtiene una lista de productos con paginación y filtrado opcional.

    Args:
        db: Sesión de base de datos.
        skip: Número de registros a omitir (para paginación).
        limit: Número máximo de registros a devolver.
        categoria: Filtro opcional por categoría.

    Returns:
        List[ProductoRead]: Lista de productos que cumplen con los criterios.
    """
    return get_productos(db=db, skip=skip, limit=limit, categoria=categoria)


@router.put("/{producto_id}", response_model=ProductoRead)
def update_producto_route(
    producto_id: int,
    producto_update: ProductoUpdate,
    db: Session = Depends(get_session),
) -> Any:
    """Actualiza un producto existente.

    Args:
        producto_id: ID del producto a actualizar.
        producto_update: Datos actualizados del producto.
        db: Sesión de base de datos.

    Returns:
        ProductoRead: El producto actualizado.
    """
    return update_producto(
        db=db, producto_id=producto_id, producto_update=producto_update
    )


@router.delete("/{producto_id}", response_model=Dict[str, Any])
def delete_producto_route(producto_id: int, db: Session = Depends(get_session)) -> Any:
    """Elimina un producto por su ID.

    Args:
        producto_id: ID del producto a eliminar.
        db: Sesión de base de datos.

    Returns:
        Dict[str, Any]: Mensaje de confirmación.
    """
    return delete_producto(db=db, producto_id=producto_id)
