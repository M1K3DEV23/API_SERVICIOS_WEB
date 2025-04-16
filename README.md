# 🚀 Servicios Web API

Bienvenido a **Servicios Web API**: una aplicación moderna desarrollada con Python 3.12.10, FastAPI, SQLModel y Pydantic-Settings, que utiliza SQLite como base de datos. Este proyecto está diseñado para ofrecer endpoints RESTful robustos y escalables para la gestión de productos, joyería y videojuegos.

## 🏗️ Arquitectura y Tecnologías

- **Lenguaje:** Python 3.12.10
- **Framework principal:** FastAPI ⚡
- **ORM:** SQLModel
- **Validación y configuración:** Pydantic & Pydantic-Settings
- **Base de datos:** SQLite
- **Documentación automática:** Swagger UI (integrado en FastAPI)

## 📦 Estructura del Proyecto

```text
Servicios_web_API/
├── app/
│   ├── core/
│   ├── modules/
│   │   ├── productos/
│   └── main.py
├── sql_app.db
└── README.md
```

## ⚙️ Instalación

1. **Clona el repositorio:**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Servicios_web_API
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**

   Puedes instalar todas las dependencias del proyecto usando el archivo `pyproject.toml` con [pip](https://pip.pypa.io/en/stable/):

   ```bash
   pip install -r requirements.txt
   ```

   O bien, si tu versión de pip no soporta instalación directa desde pyproject.toml, utiliza [pdm](https://pdm.fming.dev/) o [poetry](https://python-poetry.org/):

   ```bash
   # Usando pdm
   pdm install
   # Usando poetry
   poetry install
   ```

   Si prefieres instalar manualmente:

   ```bash
   pip install fastapi==0.110.0 sqlmodel==0.0.16 pydantic-settings==2.2.1 uvicorn==0.29.0
   ```

## 🚦 Ejecución del Proyecto

1. **Inicializa la base de datos (si es necesario):**

   - El proyecto crea automáticamente la base de datos SQLite (`sql_app.db`) al ejecutarse por primera vez.
2. **Inicia la aplicación:**

   ```bash
   python -m app.main
   ```

   - Por defecto, FastAPI se ejecutará en `http://127.0.0.1:8000`.
3. **Accede a la documentación interactiva:**

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🧩 Endpoints Principales

- `/productos/` — Gestión de productos generales

Cada módulo cuenta con endpoints para **crear, leer, actualizar y eliminar** (CRUD) registros.

## 📝 Ejemplo de Uso (cURL)

```bash
# Crear un producto
curl -X POST "http://127.0.0.1:8000/productos/" -H "Content-Type: application/json" -d '{"nombre":"Producto X","precio":99.99,"stock":10}'
```

## 🛡️ Buenas Prácticas

- El archivo `pyproject.toml` define las dependencias y la configuración del proyecto, facilitando la instalación y el mantenimiento.
- Sigue el tipado y validaciones estrictas de los modelos Pydantic/SQLModel.
- Utiliza entornos virtuales para aislar dependencias.
- Consulta la documentación interactiva para probar y entender los endpoints.

## 👨‍💻 Autor

- Desarrollado por: [Miguel Angel Rios Yañez]
- Contacto: [mikery2310@outlook.com]

---
