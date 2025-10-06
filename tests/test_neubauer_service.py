import unittest
from app.services.neubauer_service import NeubauerService
from app.models.neubauer import NeubauerRequest, NeubauerError

class TestNeubauerService(unittest.TestCase):
    """Pruebas para el servicio de Neubauer."""
    
    def test_basic_calculation(self):
        """Prueba cálculo básico de Neubauer."""
        request = NeubauerRequest(
            num_quadrants=4,
            quadrant_volume=0.1,
            dilution_factor=1,
            cell_counts=[25, 30, 28, 27]
        )
        result = NeubauerService.calculate_concentration(request)
        
        # Verificar cálculos
        expected_total = 110
        expected_average = 27.5
        expected_concentration = (27.5 / (4 * 0.1)) * 1000 * 1
        
        self.assertEqual(result.total_cells, expected_total)
        self.assertEqual(result.average_cells, expected_average)
        self.assertEqual(result.concentration, expected_concentration)
    
    def test_calculation_with_dilution(self):
        """Prueba cálculo con factor de dilución."""
        request = NeubauerRequest(
            num_quadrants=2,
            quadrant_volume=0.1,
            dilution_factor=10,
            cell_counts=[50, 45]
        )
        result = NeubauerService.calculate_concentration(request)
        
        # Con dilución 10x, la concentración final debería ser 10 veces mayor
        expected_concentration = (47.5 / (2 * 0.1)) * 1000 * 10
        self.assertEqual(result.concentration, expected_concentration)
        self.assertEqual(result.dilution_factor, 10)
    
    def test_single_quadrant(self):
        """Prueba cálculo con un solo cuadrante."""
        request = NeubauerRequest(
            num_quadrants=1,
            quadrant_volume=0.1,
            dilution_factor=1,
            cell_counts=[35]
        )
        result = NeubauerService.calculate_concentration(request)
        
        self.assertEqual(result.total_cells, 35)
        self.assertEqual(result.average_cells, 35.0)
        self.assertEqual(result.num_quadrants, 1)
    
    def test_zero_cells(self):
        """Prueba cálculo con cero células."""
        request = NeubauerRequest(
            num_quadrants=4,
            quadrant_volume=0.1,
            dilution_factor=1,
            cell_counts=[0, 0, 0, 0]
        )
        result = NeubauerService.calculate_concentration(request)
        
        self.assertEqual(result.total_cells, 0)
        self.assertEqual(result.average_cells, 0.0)
        self.assertEqual(result.concentration, 0.0)
    
    def test_invalid_num_quadrants(self):
        """Prueba validación de número de cuadrantes inválido."""
        request = NeubauerRequest(
            num_quadrants=0,  # Inválido
            quadrant_volume=0.1,
            dilution_factor=1,
            cell_counts=[]
        )
        with self.assertRaises(NeubauerError):
            NeubauerService.calculate_concentration(request)
    
    def test_invalid_quadrant_volume(self):
        """Prueba validación de volumen de cuadrante inválido."""
        request = NeubauerRequest(
            num_quadrants=1,
            quadrant_volume=0,  # Inválido
            dilution_factor=1,
            cell_counts=[10]
        )
        with self.assertRaises(NeubauerError):
            NeubauerService.calculate_concentration(request)
    
    def test_invalid_dilution_factor(self):
        """Prueba validación de factor de dilución inválido."""
        request = NeubauerRequest(
            num_quadrants=1,
            quadrant_volume=0.1,
            dilution_factor=0,  # Inválido
            cell_counts=[10]
        )
        with self.assertRaises(NeubauerError):
            NeubauerService.calculate_concentration(request)
    
    def test_mismatched_cell_counts(self):
        """Prueba validación de conteos que no coinciden con cuadrantes."""
        request = NeubauerRequest(
            num_quadrants=4,
            quadrant_volume=0.1,
            dilution_factor=1,
            cell_counts=[10, 20]  # Solo 2 conteos para 4 cuadrantes
        )
        with self.assertRaises(NeubauerError):
            NeubauerService.calculate_concentration(request)
    
    def test_negative_cell_counts(self):
        """Prueba validación de conteos negativos."""
        request = NeubauerRequest(
            num_quadrants=2,
            quadrant_volume=0.1,
            dilution_factor=1,
            cell_counts=[10, -5]  # Conteo negativo inválido
        )
        with self.assertRaises(NeubauerError):
            NeubauerService.calculate_concentration(request)
    
    def test_validate_parameters_function(self):
        """Prueba función de validación de parámetros."""
        # Parámetros válidos
        try:
            NeubauerService.validate_parameters(4, 0.1, 1.0, [10, 20, 30, 40])
        except NeubauerError:
            self.fail("validate_parameters() lanzó NeubauerError con parámetros válidos")
        
        # Parámetros inválidos
        with self.assertRaises(NeubauerError):
            NeubauerService.validate_parameters(-1, 0.1, 1.0, [10])

if __name__ == '__main__':
    unittest.main()