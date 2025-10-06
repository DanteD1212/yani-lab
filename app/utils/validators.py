"""Validadores para los formularios de la aplicación."""

def validate_numeric_input(value_str: str, field_name: str = "valor") -> float:
    """
    Valida que un string sea un número válido.
    
    Args:
        value_str: String a validar
        field_name: Nombre del campo para el mensaje de error
        
    Returns:
        float: El valor numérico
        
    Raises:
        ValueError: Si el valor no es numérico
    """
    if not value_str or value_str.strip() == "":
        raise ValueError(f"El {field_name} no puede estar vacío")
    
    try:
        value = float(value_str)
        if value < 0:
            raise ValueError(f"El {field_name} no puede ser negativo")
        return value
    except ValueError as e:
        if "cannot be negative" in str(e):
            raise
        raise ValueError(f"El {field_name} debe ser un número válido")

def validate_integer_input(value_str: str, field_name: str = "valor") -> int:
    """
    Valida que un string sea un entero válido.
    
    Args:
        value_str: String a validar
        field_name: Nombre del campo para el mensaje de error
        
    Returns:
        int: El valor entero
        
    Raises:
        ValueError: Si el valor no es un entero válido
    """
    if not value_str or value_str.strip() == "":
        raise ValueError(f"El {field_name} no puede estar vacío")
    
    try:
        value = int(value_str)
        if value <= 0:
            raise ValueError(f"El {field_name} debe ser mayor a cero")
        return value
    except ValueError as e:
        if "must be greater than zero" in str(e):
            raise
        raise ValueError(f"El {field_name} debe ser un número entero válido")

def validate_required_field(value: str, field_name: str) -> str:
    """
    Valida que un campo requerido no esté vacío.
    
    Args:
        value: Valor a validar
        field_name: Nombre del campo
        
    Returns:
        str: El valor validado
        
    Raises:
        ValueError: Si el campo está vacío
    """
    if not value or value.strip() == "":
        raise ValueError(f"El campo {field_name} es requerido")
    return value.strip()