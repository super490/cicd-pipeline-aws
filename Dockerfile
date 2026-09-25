# --- Etapa 1: Build (Instalación de dependencias) ---
FROM python:3.11-slim AS builder

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Etapa 2: Runtime (Imagen final ligera) ---
FROM python:3.11-slim AS runner

WORKDIR /app

# Copiamos el entorno virtual compilado desde el builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Seguridad DevSecOps: Usuario no-root
RUN addgroup --system appgroup && adduser --system --group appuser

COPY app/ ./app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]