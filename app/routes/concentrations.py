from flask import Blueprint, render_template, request
from ..services.concentration_service import ConcentrationService
from ..models.concentration import ConcentrationRequest, ConcentrationError, CalculationType
from ..utils.validators import validate_numeric_input, validate_required_field

bp = Blueprint('concentrations', __name__)

@bp.route('/concentraciones', methods=['GET', 'POST'])
def concentrations():
    """Página de cálculos de concentraciones."""
    if request.method == 'GET':
        calculation_types = ConcentrationService.get_calculation_types()
        return render_template('concentraciones.html', 
                             calculation_types=calculation_types,
                             resultado=None,
                             error=None)
    
    # Variables para mantener el estado del formulario
    resultado = None
    error = None
    calculation_types = ConcentrationService.get_calculation_types()
    
    try:
        # Obtener tipo de cálculo
        calc_type_str = request.form.get('calculation_type', '')
        validate_required_field(calc_type_str, 'tipo de cálculo')
        
        try:
            calc_type = CalculationType(calc_type_str)
        except ValueError:
            raise ValueError("Tipo de cálculo no válido")
        
        # Crear solicitud según el tipo de cálculo
        concentration_request = _create_request_from_form(request.form, calc_type)
        
        # Realizar cálculo
        resultado = ConcentrationService.calculate(concentration_request)
        
    except ValueError as e:
        error = str(e)
    except ConcentrationError as e:
        error = str(e)
    except Exception:
        error = "Ha ocurrido un error inesperado. Por favor, inténtalo de nuevo."
    
    return render_template('concentraciones.html', 
                         calculation_types=calculation_types,
                         resultado=resultado,
                         error=error,
                         form_data=request.form)

def _create_request_from_form(form_data, calc_type: CalculationType) -> ConcentrationRequest:
    """Crea una solicitud de concentración a partir de los datos del formulario."""
    
    def get_optional_float(field_name):
        """Obtiene un valor float opcional del formulario."""
        value = form_data.get(field_name, '').strip()
        if not value:
            return None
        return validate_numeric_input(value, field_name)
    
    request_data = {
        'calculation_type': calc_type
    }
    
    if calc_type == CalculationType.MOLARITY:
        request_data.update({
            'moles': get_optional_float('moles'),
            'volume_l': get_optional_float('volume_l'),
            'molarity': get_optional_float('molarity'),
            'mass_g': get_optional_float('mass_g'),
            'molecular_weight': get_optional_float('molecular_weight')
        })
        
    elif calc_type == CalculationType.MOLALITY:
        request_data.update({
            'moles': get_optional_float('moles'),
            'kg_solvent': get_optional_float('kg_solvent'),
            'molality': get_optional_float('molality')
        })
        
    elif calc_type == CalculationType.DILUTION:
        request_data.update({
            'c1': get_optional_float('c1'),
            'v1': get_optional_float('v1'),
            'c2': get_optional_float('c2'),
            'v2': get_optional_float('v2')
        })
        
    elif calc_type == CalculationType.MASS_VOLUME:
        request_data.update({
            'mass_g': get_optional_float('mass_g'),
            'volume_ml': get_optional_float('volume_ml'),
            'concentration_mg_ml': get_optional_float('concentration_mg_ml')
        })
        
    elif calc_type == CalculationType.PPM:
        request_data.update({
            'ppm': get_optional_float('ppm_field'),
            'percentage': get_optional_float('percentage_field'),
            'concentration_mg_ml': get_optional_float('concentration_mg_ml_field')
        })
        
    elif calc_type == CalculationType.PERCENTAGE:
        request_data.update({
            'percentage': get_optional_float('percentage_only'),
            'ppm': get_optional_float('ppm_only')
        })
    
    return ConcentrationRequest(**request_data)