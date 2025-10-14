from dataclasses import dataclass
from enum import Enum
from typing import Optional

class PHCalculationType(Enum):
    """Tipos de cálculo disponibles para la herramienta de pH."""
    STRONG_ACID = "acido_fuerte"
    STRONG_BASE = "base_fuerte"

@dataclass
class PHRequest:
    """Datos necesarios para calcular el pH de una solución."""
    calculation_type: PHCalculationType
    concentration_m: float
    equivalents: float = 1.0
    kw: float = 1e-14

@dataclass
class PHResult:
    """Resultado del cálculo de pH."""
    calculation_type: PHCalculationType
    ph: float
    poh: float
    hydronium: float
    hydroxide: float
    formula_used: str
    notes: Optional[str] = None

class PHError(Exception):
    """Excepción personalizada para errores en el cálculo de pH."""
    pass
