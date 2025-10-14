import math
from typing import Dict, List, Tuple

from ..models.ph import PHCalculationType, PHError, PHRequest, PHResult


class PHService:
    """Servicio para cálculos relacionados con pH de soluciones fuertes."""

    MIN_CONCENTRATION = 1e-12
    MAX_CONCENTRATION = 1e2
    DEFAULT_KW = 1e-14
    VERY_DILUTE_NOTE = "La solución es muy diluida, se considera el aporte del agua pura."

    _CALCULATION_MAP = {
        PHCalculationType.STRONG_ACID: "_calculate_strong_acid",
        PHCalculationType.STRONG_BASE: "_calculate_strong_base",
    }

    @classmethod
    def get_default_kw(cls) -> float:
        """Expose el valor por defecto de Kw para mantener la arquitectura en servicios."""

        return cls.DEFAULT_KW

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

        cls._validate_request(request)
        kw = cls._normalize_kw(request.kw)
        effective_concentration, notes = cls._resolve_effective_concentration(
            request.concentration_m, request.equivalents
        )

        calculator = cls._get_calculator(request.calculation_type)
        hydronium, hydroxide, formula = calculator(effective_concentration, kw)

        return cls._build_result(
            calculation_type=request.calculation_type,
            hydronium=hydronium,
            hydroxide=hydroxide,
            formula=formula,
            notes=notes,
        )

    @classmethod
    def _validate_request(cls, request: PHRequest) -> None:
        if request.concentration_m is None:
            raise PHError("Debes proporcionar la concentración molar de la solución.")

        if request.concentration_m <= 0:
            raise PHError("La concentración debe ser mayor que cero.")

        if request.equivalents is None or request.equivalents <= 0:
            raise PHError("El número de equivalentes debe ser mayor que cero.")

    @classmethod
    def _normalize_kw(cls, kw: float) -> float:
        if kw and kw > 0:
            return kw
        return cls.DEFAULT_KW

    @classmethod
    def _resolve_effective_concentration(
        cls, concentration_m: float, equivalents: float
    ) -> Tuple[float, str | None]:
        effective_concentration = concentration_m * equivalents

        if effective_concentration > cls.MAX_CONCENTRATION:
            raise PHError(
                "La concentración ingresada es demasiado alta para un cálculo fiable."
            )

        if effective_concentration < cls.MIN_CONCENTRATION:
            return cls.MIN_CONCENTRATION, cls.VERY_DILUTE_NOTE

        return effective_concentration, None

    @classmethod
    def _get_calculator(cls, calculation_type: PHCalculationType):
        method_name = cls._CALCULATION_MAP.get(calculation_type)
        if not method_name:
            raise PHError("Tipo de cálculo no soportado para la herramienta de pH.")
        return getattr(cls, method_name)

    @classmethod
    def _calculate_strong_acid(cls, effective_concentration: float, kw: float):
        hydronium = effective_concentration
        hydroxide = kw / hydronium if hydronium > 0 else 0
        return cls._ensure_positive_species(
            hydronium,
            hydroxide,
            "pH = -log₁₀([H₃O⁺])",
        )

    @classmethod
    def _calculate_strong_base(cls, effective_concentration: float, kw: float):
        hydroxide = effective_concentration
        hydronium = kw / hydroxide if hydroxide > 0 else 0
        return cls._ensure_positive_species(
            hydronium,
            hydroxide,
            "pOH = -log₁₀([OH⁻])",
        )

    @staticmethod
    def _ensure_positive_species(
        hydronium: float, hydroxide: float, formula: str
    ) -> Tuple[float, float, str]:
        if hydronium <= 0 or hydroxide <= 0:
            raise PHError("No se pudo calcular el equilibrio iónico de la solución.")
        return hydronium, hydroxide, formula

    @classmethod
    def _build_result(
        cls,
        *,
        calculation_type: PHCalculationType,
        hydronium: float,
        hydroxide: float,
        formula: str,
        notes: str | None,
    ) -> PHResult:
        ph = -math.log10(hydronium)
        poh = -math.log10(hydroxide)

        # Ajustar valores extremos manteniendo consistencia 14 = pH + pOH
        ph = max(0.0, min(14.0, ph))
        poh = 14.0 - ph

        return PHResult(
            calculation_type=calculation_type,
            ph=round(ph, 4),
            poh=round(poh, 4),
            hydronium=hydronium,
            hydroxide=hydroxide,
            formula_used=formula,
            notes=notes,
        )
