
"""
Módulo: registro_logs.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Permite registrar eventos y errores en un archivo
de seguimiento del sistema.
"""

import logging
from pathlib import Path


# Ubicación de la carpeta principal del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent

# Carpeta donde se almacenarán los registros
CARPETA_LOGS = RUTA_PROYECTO / "logs"

# Crear la carpeta si todavía no existe
CARPETA_LOGS.mkdir(exist_ok=True)

# Archivo donde se guardarán los eventos y errores
ARCHIVO_LOG = CARPETA_LOGS / "software_fj.log"


# Configuración del registro de eventos
logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)

# Evitar agregar varios controladores al importar el módulo
if not logger.handlers:

    manejador = logging.FileHandler(
        ARCHIVO_LOG,
        encoding="utf-8"
    )

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    manejador.setFormatter(formato)

    logger.addHandler(manejador)


def registrar_evento(mensaje):
    """
    Registra un evento normal del sistema.
    """
    logger.info(mensaje)


def registrar_error(mensaje):
    """
    Registra un error ocurrido durante la ejecución.
    """
    logger.error(mensaje)
