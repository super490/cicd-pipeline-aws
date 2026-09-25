import os
from fastapi import FastAPI

app = FastAPI(title="DevOps Portfolio API", version="1.0.0")

# 1. Leemos la variable. (Si Docker no la envía, asumimos "production" por seguridad)
entorno = os.getenv("ENV", "production")

@app.get("/")
def read_root():
    
    # 2. AQUÍ es donde configuras qué hace tu app en cada estado
    
    if entorno == "local":
        # --- CONFIGURACIÓN PARA LOCAL ---
        mensaje = "API running smoothly (Modo Desarrollo)"
        nivel_log = "DEBUG"
        # Aquí podrías conectar a una BD de prueba, etc.
        
    else:
        # --- CONFIGURACIÓN PARA PRODUCCIÓN ---
        mensaje = "API running smoothly (Modo Producción)"
        nivel_log = "ERROR"
        # Aquí conectarías a la BD real, etc.

    return {
        "status": "ok", 
        "message": mensaje,
        "environment": entorno,
        "log_level": nivel_log
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}