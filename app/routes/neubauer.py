from flask import Blueprint, render_template, request
from ..services.neubauer_service import NeubauerService
from ..models.neubauer import NeubauerRequest, NeubauerError
from ..utils.validators import validate_numeric_input, validate_integer_input

bp = Blueprint('neubauer', __name__)

@bp.route('/neubauer', methods=['GET', 'POST'])
def neubauer():
    """Página de cálculos de Neubauer."""
    if request.method == 'GET':
        return render_template('neubauer.html')
    
    resultado = None
    error = None
    
    try:
        # Obtener y validar parámetros básicos
        num_cuadrantes = validate_integer_input(
            request.form.get('numCuadrantes', ''), 
            'número de cuadrantes'
        )
        
        volumen_cuadrante = validate_numeric_input(
            request.form.get('volumenCuadrante', ''), 
            'volumen del cuadrante'
        )
        
        factor_dilucion = validate_numeric_input(
            request.form.get('factorDilucion', ''), 
            'factor de dilución'
        )
        
        # Obtener conteos de células para cada cuadrante
        celdas = []
        for i in range(1, num_cuadrantes + 1):
            cell_count_str = request.form.get(f'celdasCuadrante{i}', '')
            if not cell_count_str:
                raise ValueError(f"El conteo de células del cuadrante {i} es requerido")
            
            try:
                cell_count = int(cell_count_str)
                if cell_count < 0:
                    raise ValueError(f"El conteo de células del cuadrante {i} no puede ser negativo")
                celdas.append(cell_count)
            except ValueError as e:
                if "cannot be negative" in str(e):
                    raise
                raise ValueError(f"El conteo de células del cuadrante {i} debe ser un número entero válido")
        
        # Crear solicitud de cálculo
        neubauer_request = NeubauerRequest(
            num_quadrants=num_cuadrantes,
            quadrant_volume=volumen_cuadrante,
            dilution_factor=factor_dilucion,
            cell_counts=celdas
        )
        
        # Realizar cálculo
        resultado = NeubauerService.calculate_concentration(neubauer_request)
        
    except ValueError as e:
        error = str(e)
    except NeubauerError as e:
        error = str(e)
    except KeyError as e:
        error = "Faltan datos en el formulario. Por favor, completa todos los campos."
    except Exception as e:
        error = "Ha ocurrido un error inesperado. Por favor, inténtalo de nuevo."
    
    return render_template('neubauer.html', resultado=resultado, error=error)