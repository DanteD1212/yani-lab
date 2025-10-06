from ..models.neubauer import NeubauerRequest, NeubauerResult, NeubauerError

class NeubauerService:
    """Servicio para realizar cálculos de concentración celular usando la cámara de Neubauer."""
    
    @staticmethod
    def calculate_concentration(request: NeubauerRequest) -> NeubauerResult:
        """
        Calcula la concentración celular utilizando la fórmula de Neubauer.
        
        Args:
            request: Solicitud con todos los parámetros necesarios para el cálculo
            
        Returns:
            NeubauerResult con el resultado del cálculo
            
        Raises:
            NeubauerError: Si hay algún error en los parámetros o cálculo
        """
        try:
            # Validaciones básicas
            if request.num_quadrants <= 0:
                raise NeubauerError("El número de cuadrantes debe ser mayor a 0")
            
            if request.quadrant_volume <= 0:
                raise NeubauerError("El volumen del cuadrante debe ser mayor a 0")
            
            if request.dilution_factor <= 0:
                raise NeubauerError("El factor de dilución debe ser mayor a 0")
            
            if len(request.cell_counts) != request.num_quadrants:
                raise NeubauerError(
                    f"El número de conteos ({len(request.cell_counts)}) no coincide "
                    f"con el número de cuadrantes ({request.num_quadrants})"
                )
            
            if any(count < 0 for count in request.cell_counts):
                raise NeubauerError("Los conteos de células no pueden ser negativos")
            
            # Cálculos
            total_cells = sum(request.cell_counts)
            average_cells = total_cells / request.num_quadrants
            volume_total_counted = request.num_quadrants * request.quadrant_volume
            
            # Concentración en mm³
            concentration_per_mm3 = average_cells / volume_total_counted
            
            # Conversión a mL (1 mL = 1000 mm³) y aplicar factor de dilución
            concentration_per_ml = concentration_per_mm3 * 1000 * request.dilution_factor
            
            return NeubauerResult(
                concentration=concentration_per_ml,
                total_cells=total_cells,
                average_cells=average_cells,
                num_quadrants=request.num_quadrants,
                volume_per_quadrant=request.quadrant_volume,
                dilution_factor=request.dilution_factor
            )
            
        except Exception as e:
            if isinstance(e, NeubauerError):
                raise
            raise NeubauerError(f"Error en el cálculo de Neubauer: {str(e)}")
    
    @staticmethod
    def validate_parameters(num_quadrants: int, quadrant_volume: float, 
                          dilution_factor: float, cell_counts: list) -> None:
        """
        Valida los parámetros antes de crear una solicitud.
        
        Args:
            num_quadrants: Número de cuadrantes
            quadrant_volume: Volumen por cuadrante
            dilution_factor: Factor de dilución
            cell_counts: Lista de conteos de células
            
        Raises:
            NeubauerError: Si algún parámetro es inválido
        """
        if not isinstance(num_quadrants, int) or num_quadrants <= 0:
            raise NeubauerError("El número de cuadrantes debe ser un entero positivo")
        
        if not isinstance(quadrant_volume, (int, float)) or quadrant_volume <= 0:
            raise NeubauerError("El volumen del cuadrante debe ser un número positivo")
        
        if not isinstance(dilution_factor, (int, float)) or dilution_factor <= 0:
            raise NeubauerError("El factor de dilución debe ser un número positivo")
        
        if not isinstance(cell_counts, list):
            raise NeubauerError("Los conteos de células deben ser una lista")
        
        if len(cell_counts) != num_quadrants:
            raise NeubauerError(
                f"El número de conteos ({len(cell_counts)}) no coincide "
                f"con el número de cuadrantes ({num_quadrants})"
            )