import unittest
from app.services.conversion_service import ConversionService
from app.models.conversion import ConversionRequest, ConversionError, UnitType

class TestConversionService(unittest.TestCase):
    """Pruebas para el servicio de conversiones."""
    
    def test_mass_conversion_grams_to_kilograms(self):
        """Prueba conversión de gramos a kilogramos."""
        request = ConversionRequest(
            value=1000,
            from_unit='gramos',
            to_unit='kilogramos',
            unit_type=UnitType.MASS
        )
        result = ConversionService.convert(request)
        self.assertEqual(result.converted_value, 1.0)
    
    def test_mass_conversion_kilograms_to_grams(self):
        """Prueba conversión de kilogramos a gramos."""
        request = ConversionRequest(
            value=2.5,
            from_unit='kilogramos',
            to_unit='gramos',
            unit_type=UnitType.MASS
        )
        result = ConversionService.convert(request)
        self.assertEqual(result.converted_value, 2500.0)
    
    def test_temperature_conversion_celsius_to_fahrenheit(self):
        """Prueba conversión de Celsius a Fahrenheit."""
        request = ConversionRequest(
            value=0,
            from_unit='celsius',
            to_unit='fahrenheit',
            unit_type=UnitType.TEMPERATURE
        )
        result = ConversionService.convert(request)
        self.assertEqual(result.converted_value, 32.0)
    
    def test_temperature_conversion_fahrenheit_to_celsius(self):
        """Prueba conversión de Fahrenheit a Celsius."""
        request = ConversionRequest(
            value=32,
            from_unit='fahrenheit',
            to_unit='celsius',
            unit_type=UnitType.TEMPERATURE
        )
        result = ConversionService.convert(request)
        self.assertEqual(result.converted_value, 0.0)
    
    def test_volume_conversion_liters_to_milliliters(self):
        """Prueba conversión de litros a mililitros."""
        request = ConversionRequest(
            value=1.5,
            from_unit='litros',
            to_unit='mililitros',
            unit_type=UnitType.VOLUME
        )
        result = ConversionService.convert(request)
        self.assertEqual(result.converted_value, 1500.0)
    
    def test_same_unit_conversion(self):
        """Prueba conversión entre la misma unidad."""
        request = ConversionRequest(
            value=100,
            from_unit='gramos',
            to_unit='gramos',
            unit_type=UnitType.MASS
        )
        result = ConversionService.convert(request)
        self.assertEqual(result.converted_value, 100.0)
    
    def test_unsupported_conversion(self):
        """Prueba conversión no soportada."""
        request = ConversionRequest(
            value=100,
            from_unit='gramos',
            to_unit='libras',  # Unidad no soportada
            unit_type=UnitType.MASS
        )
        with self.assertRaises(ConversionError):
            ConversionService.convert(request)
    
    def test_get_available_units(self):
        """Prueba obtener unidades disponibles."""
        mass_units = ConversionService.get_available_units(UnitType.MASS)
        self.assertIn('gramos', mass_units)
        self.assertIn('kilogramos', mass_units)
        
        temp_units = ConversionService.get_available_units(UnitType.TEMPERATURE)
        self.assertIn('celsius', temp_units)
        self.assertIn('fahrenheit', temp_units)

if __name__ == '__main__':
    unittest.main()