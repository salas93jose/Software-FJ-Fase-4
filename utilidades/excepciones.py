
"""
Módulo: excepciones.py
Proyecto: Sistema Integral de Gestión de Clientes,
Servicios y Reservas - Software FJ.

Define las excepciones personalizadas utilizadas
para controlar los errores del sistema.
"""


class ErrorSoftwareFJ(Exception):
    """
    Excepción base del sistema.

    Las demás excepciones personalizadas heredarán
    de esta clase.
    """
    pass


class ErrorValidacion(ErrorSoftwareFJ):
    """
    Se presenta cuando los datos ingresados
    no cumplen las validaciones establecidas.
    """
    pass


class ErrorServicio(ErrorSoftwareFJ):
    """
    Se presenta cuando ocurre un problema
    relacionado con la creación o disponibilidad
    de un servicio.
    """
    pass


class ErrorReserva(ErrorSoftwareFJ):
    """
    Se presenta cuando una reserva no puede
    crearse, confirmarse, cancelarse o procesarse.
    """
    pass


class ErrorOperacion(ErrorSoftwareFJ):
    """
    Se presenta cuando se intenta ejecutar
    una operación no permitida por el sistema.
    """
    pass
