from flask import Blueprint, render_template, request
from ..services.conversion_service import ConversionService
from ..models.conversion import ConversionRequest, ConversionError, UnitType
from ..utils.validators import validate_numeric_input, validate_required_field

bp = Blueprint('conversions', __name__)

@bp.route('/conversiones', methods=['GET', 'POST'])
def conversions():
    """Página de conversiones de unidades."""
    if request.method == 'GET':
        return render_template('conversiones.html', 
                             resultado=None,
                             error=None,
                             valor='',
                             unidad_origen='',
                             unidad_destino='',
                             tipo_unidad='')
    
    # Variables para mantener el estado del formulario
    resultado = None
    error = None
    valor_str = request.form.get('valor', '')
    unidad_origen = request.form.get('unidad_origen', '')
    unidad_destino = request.form.get('unidad_destino', '')
    tipo_unidad = request.form.get('tipo_unidad', '')
    
    try:
        # Validar campos requeridos
        validate_required_field(valor_str, 'valor')
        validate_required_field(unidad_origen, 'unidad origen')
        validate_required_field(unidad_destino, 'unidad destino')
        validate_required_field(tipo_unidad, 'tipo de unidad')
        
        # Validar valor numérico
        valor = validate_numeric_input(valor_str, 'valor')
        
        # Validar tipo de unidad
        try:
            unit_type = UnitType(tipo_unidad)
        except ValueError:
            raise ValueError("Tipo de unidad no válido")
        
        # Crear solicitud de conversión
        conversion_request = ConversionRequest(
            value=valor,
            from_unit=unidad_origen,
            to_unit=unidad_destino,
            unit_type=unit_type
        )
        
        # Realizar conversión
        result = ConversionService.convert(conversion_request)
        resultado = result.converted_value
        
    except ValueError as e:
        error = str(e)
    except ConversionError as e:
        error = str(e)
    except Exception as e:
        error = "Ha ocurrido un error inesperado. Por favor, inténtalo de nuevo."
    
    return render_template('conversiones.html', 
                         resultado=resultado,
                         error=error,
                         valor=valor_str,
                         unidad_origen=unidad_origen,
                         unidad_destino=unidad_destino,
                         tipo_unidad=tipo_unidad)