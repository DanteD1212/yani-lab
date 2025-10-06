from dataclasses import dataclass
from typing import List

@dataclass
class NeubauerRequest:
    """Representa una solicitud de cálculo de Neubauer."""
    num_quadrants: int
    quadrant_volume: float
    dilution_factor: float
    cell_counts: List[int]

@dataclass
class NeubauerResult:
    """Resultado de un cálculo de Neubauer."""
    concentration: float
    total_cells: int
    average_cells: float
    num_quadrants: int
    volume_per_quadrant: float
    dilution_factor: float

class NeubauerError(Exception):
    """Excepción personalizada para errores en cálculos de Neubauer."""
    pass