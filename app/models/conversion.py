from dataclasses import dataclass
from enum import Enum
from typing import Dict, Callable

class UnitType(Enum):
    """Tipos de unidades soportadas por el sistema."""
    MASS = "masa"
    TEMPERATURE = "temperatura" 
    VOLUME = "volumen"

@dataclass
class ConversionRequest:
    """Representa una solicitud de conversión de unidades."""
    value: float
    from_unit: str
    to_unit: str
    unit_type: UnitType

@dataclass
class ConversionResult:
    """Resultado de una conversión de unidades."""
    original_value: float
    converted_value: float
    from_unit: str
    to_unit: str
    unit_type: UnitType
    
class ConversionError(Exception):
    """Excepción personalizada para errores de conversión."""
    pass