"""Módulo que define los modelos de datos para productos."""

from datetime import datetime
from typing import Optional

from pydantic import field_validator
from sqlmodel import Field, SQLModel


class ProductoBase(SQLModel):
    """Modelo base para productos.

    Attributes:
        nombre: Nombre del producto.
        descripcion: Descripción detallada del producto.
        precio: Precio del producto en formato decimal.
        stock: Cantidad disponible en inventario.
        categoria: Categoría a la que pertenece el producto.
    """

    nombre: str = Field(
        ..., min_length=1, max_length=100, description="Nombre del producto"
    )
    descripcion: Optional[str] = Field(
        default=None, max_length=500, description="Descripción del producto"
    )
    precio: float = Field(..., gt=0, description="Precio del producto")
    stock: int = Field(..., ge=0, description="Cantidad disponible en inventario")
    categoria: Optional[str] = Field(
        default=None, max_length=50, description="Categoría del producto"
    )

    @field_validator("precio")
    def validate_precio(cls, v):
        """Valida que el precio tenga un formato válido."""
        if v <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        return round(v, 2)  # Redondear a 2 decimales


class Producto(ProductoBase, table=True):
    """Modelo de producto para la base de datos.

    Attributes:
        id: Identificador único del producto.
        fecha_creacion: Fecha de creación del producto.
        fecha_actualizacion: Fecha de última actualización del producto.
    """

    __tablename__ = "productos"

    id: Optional[int] = Field(default=None, primary_key=True)
    fecha_creacion: datetime = Field(default_factory=datetime.now)
    fecha_actualizacion: Optional[datetime] = Field(default=None)


class ProductoCreate(ProductoBase):
    """Esquema para crear un nuevo producto."""

    pass


class ProductoUpdate(SQLModel):
    """Esquema para actualizar un producto existente.

    Todos los campos son opcionales para permitir actualizaciones parciales.
    """

    nombre: Optional[str] = Field(default=None, min_length=1, max_length=100)
    descripcion: Optional[str] = Field(default=None, max_length=500)
    precio: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)
    categoria: Optional[str] = Field(default=None, max_length=50)


class ProductoRead(ProductoBase):
    """Esquema para leer un producto.

    Incluye todos los campos del modelo base más el ID y fechas.
    """

    id: int
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None
