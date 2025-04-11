FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Optimizar la compilación y el manejo de caché
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del proyecto
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Agregar el código fuente e instalar el proyecto
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Configurar el entorno
ENV PATH="/app/.venv/bin:$PATH"

# Resetear el entrypoint
ENTRYPOINT []

# Ejecutar el servidor de desarrollo de Django con recarga automática
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
