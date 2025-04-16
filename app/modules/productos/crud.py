"""Módulo que implementa las operaciones CRUD para productos."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.modules.productos.models import Producto, ProductoCreate, ProductoUpdate


def get_producto(db: Session, producto_id: int) -> Producto:
    """Obtiene un producto por su ID.

    Args:
        db: Sesión de base de datos.
        producto_id: ID del producto a buscar.

    Returns:
        Producto: El producto encontrado.

    Raises:
        HTTPException: Si el producto no existe.
    """
    producto = db.get(Producto, producto_id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con ID {producto_id} no encontrado",
        )
    return producto


def get_productos(
    db: Session, skip: int = 0, limit: int = 100, categoria: Optional[str] = None
) -> List[Producto]:
    """Obtiene una lista de productos con paginación y filtrado opcional.

    Args:
        db: Sesión de base de datos.
        skip: Número de registros a omitir (para paginación).
        limit: Número máximo de registros a devolver.
        categoria: Filtro opcional por categoría.

    Returns:
        List[Producto]: Lista de productos que cumplen con los criterios.
    """
    query = select(Producto)

    if categoria:
        query = query.where(Producto.categoria == categoria)

    return db.exec(query.offset(skip).limit(limit)).all()


def create_producto(db: Session, producto: ProductoCreate) -> Producto:
    """Crea un nuevo producto.

    Args:
        db: Sesión de base de datos.
        producto: Datos del producto a crear.

    Returns:
        Producto: El producto creado.
    """
    db_producto = Producto.from_orm(producto)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def update_producto(
    db: Session, producto_id: int, producto_update: ProductoUpdate
) -> Producto:
    """Actualiza un producto existente.

    Args:
        db: Sesión de base de datos.
        producto_id: ID del producto a actualizar.
        producto_update: Datos actualizados del producto.

    Returns:
        Producto: El producto actualizado.

    Raises:
        HTTPException: Si el producto no existe.
    """
    db_producto = get_producto(db, producto_id)

    # Convertir a diccionario y filtrar valores None
    update_data = producto_update.dict(exclude_unset=True)

    # Si no hay datos para actualizar, retornar el producto sin cambios
    if not update_data:
        return db_producto

    # Actualizar los campos del producto
    for key, value in update_data.items():
        setattr(db_producto, key, value)

    # Actualizar la fecha de actualización
    db_producto.fecha_actualizacion = datetime.utcnow()

    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def delete_producto(db: Session, producto_id: int) -> Dict[str, Any]:
    """Elimina un producto por su ID.

    Args:
        db: Sesión de base de datos.
        producto_id: ID del producto a eliminar.

    Returns:
        Dict[str, Any]: Mensaje de confirmación.

    Raises:
        HTTPException: Si el producto no existe.
    """
    db_producto = get_producto(db, producto_id)
    db.delete(db_producto)
    db.commit()
    return {
        "ok": True,
        "message": f"Producto con ID {producto_id} eliminado correctamente",
    }
