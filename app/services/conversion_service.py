from typing import Dict, Callable, List
from ..models.conversion import ConversionRequest, ConversionResult, ConversionError, UnitType

class ConversionService:
    """Servicio para manejar todas las conversiones de unidades."""
    
    # Diccionario con todas las conversiones disponibles
    _CONVERSIONS: Dict[UnitType, Dict[tuple, Callable]] = {
        UnitType.MASS: {
            ('gramos', 'kilogramos'): lambda x: x / 1000,
            ('kilogramos', 'gramos'): lambda x: x * 1000,
        },
        UnitType.TEMPERATURE: {
            ('celsius', 'fahrenheit'): lambda x: (x * 9/5) + 32,
            ('fahrenheit', 'celsius'): lambda x: (x - 32) * 5/9,
        },
        UnitType.VOLUME: {
            ('litros', 'mililitros'): lambda x: x * 1000,
            ('mililitros', 'litros'): lambda x: x / 1000,
        }
    }
    
    @classmethod
    def convert(cls, request: ConversionRequest) -> ConversionResult:
        """
        Realiza una conversión de unidades.
        
        Args:
            request: Solicitud de conversión con todos los parámetros necesarios
            
        Returns:
            ConversionResult con el resultado de la conversión
            
        Raises:
            ConversionError: Si la conversión no es soportada
        """
        # Si las unidades son iguales, no hay conversión
        if request.from_unit == request.to_unit:
            converted_value = request.value
        else:
            conversion_key = (request.from_unit, request.to_unit)
            conversions = cls._CONVERSIONS.get(request.unit_type, {})
            
            if conversion_key not in conversions:
                raise ConversionError(
                    f"Conversión no soportada: {request.from_unit} a {request.to_unit} "
                    f"para el tipo {request.unit_type.value}"
                )
            
            converted_value = conversions[conversion_key](request.value)
        
        return ConversionResult(
            original_value=request.value,
            converted_value=converted_value,
            from_unit=request.from_unit,
            to_unit=request.to_unit,
            unit_type=request.unit_type
        )
    
    @classmethod
    def get_available_units(cls, unit_type: UnitType) -> List[str]:
        """
        Retorna las unidades disponibles para un tipo dado.
        
        Args:
            unit_type: El tipo de unidad
            
        Returns:
            Lista de unidades disponibles
        """
        units = set()
        conversions = cls._CONVERSIONS.get(unit_type, {})
        for from_unit, to_unit in conversions.keys():
            units.add(from_unit)
            units.add(to_unit)
        return sorted(list(units))
    
    @classmethod
    def get_all_unit_types(cls) -> List[UnitType]:
        """Retorna todos los tipos de unidades disponibles."""
        return list(cls._CONVERSIONS.keys())