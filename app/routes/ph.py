from flask import Blueprint, render_template, request

from ..services.ph_service import PHService
from ..models.ph import PHRequest, PHError, PHCalculationType
from ..utils.validators import validate_numeric_input

bp = Blueprint('ph', __name__)

@bp.route('/ph', methods=['GET', 'POST'])
def ph_calculator():
    """Calculadora de pH para soluciones fuertes."""
    calculation_types = PHService.get_calculation_types()

    if request.method == 'GET':
        return render_template(
            'ph.html',
            calculation_types=calculation_types,
            resultado=None,
            error=None,
            form_data=None
        )

    error = None
    resultado = None

    try:
        calc_type_str = request.form.get('calculation_type', '')
        if not calc_type_str:
            raise ValueError("Selecciona el tipo de solución a calcular.")

        try:
            calc_type = PHCalculationType(calc_type_str)
        except ValueError:
            raise ValueError("Tipo de cálculo no válido.")

        concentration = validate_numeric_input(
            request.form.get('concentration_m', ''),
            'concentración'
        )

        equivalents_str = request.form.get('equivalents', '1')
        equivalents = validate_numeric_input(equivalents_str, 'equivalentes')

        kw_str = request.form.get('kw', '')
        kw_value = None
        if kw_str:
            kw_value = validate_numeric_input(kw_str, 'constante iónica del agua')

        ph_request = PHRequest(
            calculation_type=calc_type,
            concentration_m=concentration,
            equivalents=equivalents,
            kw=kw_value if kw_value is not None else PHService.DEFAULT_KW
        )

        resultado = PHService.calculate(ph_request)

    except (ValueError, PHError) as exc:
        error = str(exc)
    except Exception:
        error = "Ha ocurrido un error inesperado. Por favor, inténtalo de nuevo."

    return render_template(
        'ph.html',
        calculation_types=calculation_types,
        resultado=resultado,
        error=error,
        form_data=request.form
    )
