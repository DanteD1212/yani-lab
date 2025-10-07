import unittest
from app.services.concentration_service import ConcentrationService
from app.models.concentration import ConcentrationRequest, ConcentrationError, CalculationType

class TestConcentrationService(unittest.TestCase):
    """Pruebas para el servicio de concentraciones."""
    
    def test_molarity_calculation_from_moles_and_volume(self):
        """Prueba cálculo de molaridad a partir de moles y volumen."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.MOLARITY,
            moles=0.5,
            volume_l=2.0
        )
        result = ConcentrationService.calculate(request)
        
        self.assertEqual(result.molarity, 0.25)
        self.assertEqual(result.moles, 0.5)
        self.assertEqual(result.volume_l, 2.0)
    
    def test_molarity_calculation_from_mass_and_molecular_weight(self):
        """Prueba cálculo de molaridad a partir de masa, peso molecular y volumen."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.MOLARITY,
            mass_g=58.5,  # NaCl
            molecular_weight=58.5,  # g/mol
            volume_l=1.0
        )
        result = ConcentrationService.calculate(request)
        
        self.assertEqual(result.molarity, 1.0)
        self.assertEqual(result.moles, 1.0)
        self.assertEqual(result.mass_g, 58.5)
    
    def test_molality_calculation(self):
        """Prueba cálculo de molalidad."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.MOLALITY,
            moles=2.0,
            kg_solvent=1.0
        )
        result = ConcentrationService.calculate(request)
        
        self.assertEqual(result.molality, 2.0)
        self.assertEqual(result.moles, 2.0)
    
    def test_dilution_calculation_c1(self):
        """Prueba cálculo de diluciones - calcular C1."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.DILUTION,
            v1=10.0,
            c2=0.1,
            v2=100.0
        )
        result = ConcentrationService.calculate(request)
        
        self.assertEqual(result.c1, 1.0)  # C1 = (C2 * V2) / V1 = (0.1 * 100) / 10 = 1.0
        self.assertEqual(result.v1, 10.0)
        self.assertEqual(result.c2, 0.1)
        self.assertEqual(result.v2, 100.0)
    
    def test_dilution_calculation_v2(self):
        """Prueba cálculo de diluciones - calcular V2."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.DILUTION,
            c1=2.0,
            v1=25.0,
            c2=0.5
        )
        result = ConcentrationService.calculate(request)
        
        self.assertEqual(result.v2, 100.0)  # V2 = (C1 * V1) / C2 = (2.0 * 25.0) / 0.5 = 100.0
    
    def test_mass_volume_calculation(self):
        """Prueba cálculo de concentración masa/volumen."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.MASS_VOLUME,
            mass_g=5.0,
            volume_ml=100.0
        )
        result = ConcentrationService.calculate(request)
        
        self.assertEqual(result.concentration_mg_ml, 50.0)  # (5.0 * 1000) / 100 = 50 mg/mL
        self.assertEqual(result.concentration_g_l, 50.0)    # 5.0 / (100/1000) = 50 g/L
    
    def test_ppm_conversion(self):
        """Prueba conversiones con ppm."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.PPM,
            ppm=1000.0
        )
        result = ConcentrationService.calculate(request)
        
        self.assertEqual(result.ppm, 1000.0)
        self.assertEqual(result.percentage, 0.1)  # 1000 ppm = 0.1%
        self.assertEqual(result.concentration_mg_ml, 1.0)  # 1000 ppm = 1 mg/mL
    
    def test_percentage_conversion(self):
        """Prueba conversiones de porcentaje."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.PERCENTAGE,
            percentage=5.0
        )
        result = ConcentrationService.calculate(request)
        
        self.assertEqual(result.percentage, 5.0)
        self.assertEqual(result.ppm, 50000.0)  # 5% = 50000 ppm
        self.assertEqual(result.concentration_g_l, 50.0)  # 5% = 50 g/L
    
    def test_invalid_molarity_zero_volume(self):
        """Prueba validación de volumen cero en molaridad."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.MOLARITY,
            moles=1.0,
            volume_l=0.0
        )
        with self.assertRaises(ConcentrationError):
            ConcentrationService.calculate(request)
    
    def test_invalid_dilution_insufficient_params(self):
        """Prueba validación de parámetros insuficientes en diluciones."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.DILUTION,
            c1=1.0,
            v1=10.0
            # Faltan C2 y V2
        )
        with self.assertRaises(ConcentrationError):
            ConcentrationService.calculate(request)
    
    def test_invalid_dilution_too_many_params(self):
        """Prueba validación de demasiados parámetros en diluciones."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.DILUTION,
            c1=1.0,
            v1=10.0,
            c2=0.5,
            v2=20.0  # Todos los parámetros dados
        )
        with self.assertRaises(ConcentrationError):
            ConcentrationService.calculate(request)
    
    def test_molarity_insufficient_params(self):
        """Prueba validación de parámetros insuficientes en molaridad."""
        request = ConcentrationRequest(
            calculation_type=CalculationType.MOLARITY,
            moles=1.0
            # Falta volumen o otros parámetros
        )
        with self.assertRaises(ConcentrationError):
            ConcentrationService.calculate(request)
    
    def test_get_calculation_types(self):
        """Prueba obtener tipos de cálculo disponibles."""
        calc_types = ConcentrationService.get_calculation_types()
        
        self.assertIsInstance(calc_types, list)
        self.assertTrue(len(calc_types) > 0)
        
        # Verificar que cada tipo tiene 'value' y 'label'
        for calc_type in calc_types:
            self.assertIn('value', calc_type)
            self.assertIn('label', calc_type)

if __name__ == '__main__':
    unittest.main()