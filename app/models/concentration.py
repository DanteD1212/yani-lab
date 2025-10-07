from dataclasses import dataclass
from enum import Enum
from typing import Optional

class CalculationType(Enum):
    """Tipos de cálculos de concentración soportados."""
    MOLARITY = "molaridad"
    MOLALITY = "molalidad"
    DILUTION = "dilucion"
    MASS_VOLUME = "masa_volumen"
    PPM = "ppm"
    PERCENTAGE = "porcentaje"

@dataclass
class ConcentrationRequest:
    """Representa una solicitud de cálculo de concentración."""
    calculation_type: CalculationType
    
    # Para molaridad
    moles: Optional[float] = None
    volume_l: Optional[float] = None
    molarity: Optional[float] = None
    
    # Para molalidad
    kg_solvent: Optional[float] = None
    molality: Optional[float] = None
    
    # Para diluciones (C1V1 = C2V2)
    c1: Optional[float] = None
    v1: Optional[float] = None
    c2: Optional[float] = None
    v2: Optional[float] = None
    
    # Para masa/volumen
    mass_g: Optional[float] = None
    molecular_weight: Optional[float] = None
    volume_ml: Optional[float] = None
    
    # Para concentraciones masa/volumen
    concentration_mg_ml: Optional[float] = None
    concentration_g_l: Optional[float] = None
    
    # Para ppm y porcentajes
    ppm: Optional[float] = None
    percentage: Optional[float] = None

@dataclass
class ConcentrationResult:
    """Resultado de un cálculo de concentración."""
    calculation_type: CalculationType
    
    # Resultados calculados
    molarity: Optional[float] = None
    molality: Optional[float] = None
    moles: Optional[float] = None
    volume_l: Optional[float] = None
    mass_g: Optional[float] = None
    
    # Para diluciones
    c1: Optional[float] = None
    v1: Optional[float] = None
    c2: Optional[float] = None
    v2: Optional[float] = None
    
    # Conversiones adicionales
    concentration_mg_ml: Optional[float] = None
    concentration_g_l: Optional[float] = None
    ppm: Optional[float] = None
    percentage: Optional[float] = None
    
    # Información adicional
    formula_used: Optional[str] = None
    notes: Optional[str] = None

class ConcentrationError(Exception):
    """Excepción personalizada para errores en cálculos de concentración."""
    pass