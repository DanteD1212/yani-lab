import math
from typing import List, Dict

from ..models.ph import PHRequest, PHResult, PHError, PHCalculationType

class PHService:
    """Servicio para cálculos relacionados con pH de soluciones fuertes."""

    MIN_CONCENTRATION = 1e-12
    MAX_CONCENTRATION = 1e2
    DEFAULT_KW = 1e-14

    @classmethod
    def get_calculation_types(cls) -> List[Dict[str, str]]:
        """Devuelve los tipos de cálculo disponibles para la interfaz."""
        return [
            {"value": PHCalculationType.STRONG_ACID.value, "label": "Ácido fuerte"},
            {"value": PHCalculationType.STRONG_BASE.value, "label": "Base fuerte"},
        ]

    @classmethod
    def calculate(cls, request: PHRequest) -> PHResult:
        """Calcula el pH o pOH según el tipo de solución fuerte seleccionada."""
        if request.concentration_m is None:
            raise PHError("Debes proporcionar la concentración molar de la solución.")

        if request.concentration_m <= 0:
            raise PHError("La concentración debe ser mayor que cero.")

        if request.equivalents is None or request.equivalents <= 0:
            raise PHError("El número de equivalentes debe ser mayor que cero.")

        kw = request.kw if request.kw and request.kw > 0 else cls.DEFAULT_KW
        effective_concentration = request.concentration_m * request.equivalents

        if effective_concentration < cls.MIN_CONCENTRATION:
            notes = (
                "La solución es muy diluida, se considera el aporte del agua pura."
            )
            effective_concentration = cls.MIN_CONCENTRATION
        else:
            notes = None

        if effective_concentration > cls.MAX_CONCENTRATION:
            raise PHError("La concentración ingresada es demasiado alta para un cálculo fiable.")

        if request.calculation_type == PHCalculationType.STRONG_ACID:
            hydronium = effective_concentration
            hydroxide = kw / hydronium
            formula = "pH = -log₁₀([H₃O⁺])"
        elif request.calculation_type == PHCalculationType.STRONG_BASE:
            hydroxide = effective_concentration
            hydronium = kw / hydroxide
            formula = "pOH = -log₁₀([OH⁻])"
        else:
            raise PHError("Tipo de cálculo no soportado para la herramienta de pH.")

        if hydronium <= 0 or hydroxide <= 0:
            raise PHError("No se pudo calcular el equilibrio iónico de la solución.")

        ph = -math.log10(hydronium)
        poh = -math.log10(hydroxide)

        # Ajustar valores extremos manteniendo consistencia 14 = pH + pOH
        ph = max(0.0, min(14.0, ph))
        poh = 14.0 - ph

        return PHResult(
            calculation_type=request.calculation_type,
            ph=round(ph, 4),
            poh=round(poh, 4),
            hydronium=hydronium,
            hydroxide=hydroxide,
            formula_used=formula,
            notes=notes,
        )
