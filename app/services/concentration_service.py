from ..models.concentration import ConcentrationRequest, ConcentrationResult, ConcentrationError, CalculationType

class ConcentrationService:
    """Servicio voor manejar todos los cálculos de concentración."""
    
    @classmethod
    def calculate(cls, request: ConcentrationRequest) -> ConcentrationResult:
        """
        Realiza cálculos de concentración según el tipo especificado.
        
        Args:
            request: Solicitud de cálculo con todos los parámetros necesarios
            
        Returns:
            ConcentrationResult con el resultado del cálculo
            
        Raises:
            ConcentrationError: Si faltan parámetros o hay errores en el cálculo
        """
        calculation_methods = {
            CalculationType.MOLARITY: cls._calculate_molarity,
            CalculationType.MOLALITY: cls._calculate_molality,
            CalculationType.DILUTION: cls._calculate_dilution,
            CalculationType.MASS_VOLUME: cls._calculate_mass_volume,
            CalculationType.PPM: cls._calculate_ppm,
            CalculationType.PERCENTAGE: cls._calculate_percentage,
        }
        
        method = calculation_methods.get(request.calculation_type)
        if not method:
            raise ConcentrationError(f"Tipo de cálculo no soportado: {request.calculation_type}")
        
        return method(request)
    
    @classmethod
    def _calculate_molarity(cls, request: ConcentrationRequest) -> ConcentrationResult:
        """Calcula molaridad: M = moles / volumen(L)"""
        result = ConcentrationResult(
            calculation_type=CalculationType.MOLARITY,
            formula_used="M = moles / volumen(L)"
        )
        
        # Casos posibles:
        # 1. Calcular molaridad a partir de moles y volumen
        if request.moles is not None and request.volume_l is not None:
            if request.volume_l <= 0:
                raise ConcentrationError("El volumen debe ser mayor a 0")
            result.molarity = request.moles / request.volume_l
            result.moles = request.moles
            result.volume_l = request.volume_l
            
        # 2. Calcular moles a partir de molaridad y volumen
        elif request.molarity is not None and request.volume_l is not None:
            if request.volume_l <= 0:
                raise ConcentrationError("El volumen debe ser mayor a 0")
            result.moles = request.molarity * request.volume_l
            result.molarity = request.molarity
            result.volume_l = request.volume_l
            
        # 3. Calcular volumen a partir de molaridad y moles
        elif request.molarity is not None and request.moles is not None:
            if request.molarity <= 0:
                raise ConcentrationError("La molaridad debe ser mayor a 0")
            result.volume_l = request.moles / request.molarity
            result.molarity = request.molarity
            result.moles = request.moles
            
        # 4. Calcular a partir de masa, peso molecular y volumen
        elif request.mass_g is not None and request.molecular_weight is not None and request.volume_l is not None:
            if request.molecular_weight <= 0:
                raise ConcentrationError("El peso molecular debe ser mayor a 0")
            if request.volume_l <= 0:
                raise ConcentrationError("El volumen debe ser mayor a 0")
            
            moles = request.mass_g / request.molecular_weight
            result.molarity = moles / request.volume_l
            result.moles = moles
            result.mass_g = request.mass_g
            result.volume_l = request.volume_l
            
        else:
            raise ConcentrationError("Parámetros insuficientes para calcular molaridad. "
                                   "Necesitas: (moles + volumen) o (molaridad + volumen) o "
                                   "(molaridad + moles) o (masa + peso molecular + volumen)")
        
        # Agregar conversiones adicionales
        if result.molarity is not None and request.molecular_weight is not None:
            result.concentration_g_l = result.molarity * request.molecular_weight
            result.concentration_mg_ml = result.concentration_g_l
        
        return result
    
    @classmethod
    def _calculate_molality(cls, request: ConcentrationRequest) -> ConcentrationResult:
        """Calcula molalidad: m = moles / kg_disolvente"""
        result = ConcentrationResult(
            calculation_type=CalculationType.MOLALITY,
            formula_used="m = moles / kg_disolvente"
        )
        
        # 1. Calcular molalidad a partir de moles y kg de disolvente
        if request.moles is not None and request.kg_solvent is not None:
            if request.kg_solvent <= 0:
                raise ConcentrationError("La masa del disolvente debe ser mayor a 0")
            result.molality = request.moles / request.kg_solvent
            result.moles = request.moles
            
        # 2. Calcular moles a partir de molalidad y kg de disolvente
        elif request.molality is not None and request.kg_solvent is not None:
            if request.kg_solvent <= 0:
                raise ConcentrationError("La masa del disolvente debe ser mayor a 0")
            result.moles = request.molality * request.kg_solvent
            result.molality = request.molality
            
        else:
            raise ConcentrationError("Parámetros insuficientes para calcular molalidad. "
                                   "Necesitas: (moles + kg_disolvente) o (molalidad + kg_disolvente)")
        
        return result
    
    @classmethod
    def _calculate_dilution(cls, request: ConcentrationRequest) -> ConcentrationResult:
        """Calcula diluciones: C1×V1 = C2×V2"""
        result = ConcentrationResult(
            calculation_type=CalculationType.DILUTION,
            formula_used="C₁ × V₁ = C₂ × V₂"
        )
        
        # Contar cuántos parámetros tenemos
        params = [request.c1, request.v1, request.c2, request.v2]
        non_none_params = [p for p in params if p is not None]
        
        if len(non_none_params) != 3:
            raise ConcentrationError("Para calcular diluciones necesitas exactamente 3 de los 4 parámetros: C₁, V₁, C₂, V₂")
        
        # Calcular el parámetro faltante
        if request.c1 is None:
            if request.v1 <= 0 or request.c2 <= 0 or request.v2 <= 0:
                raise ConcentrationError("Todos los valores deben ser mayores a 0")
            result.c1 = (request.c2 * request.v2) / request.v1
            result.v1 = request.v1
            result.c2 = request.c2
            result.v2 = request.v2
            
        elif request.v1 is None:
            if request.c1 <= 0 or request.c2 <= 0 or request.v2 <= 0:
                raise ConcentrationError("Todos los valores deben ser mayores a 0")
            result.v1 = (request.c2 * request.v2) / request.c1
            result.c1 = request.c1
            result.c2 = request.c2
            result.v2 = request.v2
            
        elif request.c2 is None:
            if request.c1 <= 0 or request.v1 <= 0 or request.v2 <= 0:
                raise ConcentrationError("Todos los valores deben ser mayores a 0")
            result.c2 = (request.c1 * request.v1) / request.v2
            result.c1 = request.c1
            result.v1 = request.v1
            result.v2 = request.v2
            
        elif request.v2 is None:
            if request.c1 <= 0 or request.v1 <= 0 or request.c2 <= 0:
                raise ConcentrationError("Todos los valores deben ser mayores a 0")
            result.v2 = (request.c1 * request.v1) / request.c2
            result.c1 = request.c1
            result.v1 = request.v1
            result.c2 = request.c2
        
        return result
    
    @classmethod
    def _calculate_mass_volume(cls, request: ConcentrationRequest) -> ConcentrationResult:
        """Calcula concentraciones masa/volumen"""
        result = ConcentrationResult(
            calculation_type=CalculationType.MASS_VOLUME,
            formula_used="Concentración = masa / volumen"
        )
        
        # 1. Calcular concentración a partir de masa y volumen
        if request.mass_g is not None and request.volume_ml is not None:
            if request.volume_ml <= 0:
                raise ConcentrationError("El volumen debe ser mayor a 0")
            result.concentration_mg_ml = (request.mass_g * 1000) / request.volume_ml  # mg/mL
            result.concentration_g_l = request.mass_g / (request.volume_ml / 1000)    # g/L
            result.mass_g = request.mass_g
            
        # 2. Calcular masa a partir de concentración y volumen
        elif request.concentration_mg_ml is not None and request.volume_ml is not None:
            if request.volume_ml <= 0:
                raise ConcentrationError("El volumen debe ser mayor a 0")
            result.mass_g = (request.concentration_mg_ml * request.volume_ml) / 1000
            result.concentration_mg_ml = request.concentration_mg_ml
            result.concentration_g_l = request.concentration_mg_ml  # mg/mL = g/L
            
        else:
            raise ConcentrationError("Parámetros insuficientes para calcular concentración masa/volumen. "
                                   "Necesitas: (masa + volumen) o (concentración + volumen)")
        
        return result
    
    @classmethod
    def _calculate_ppm(cls, request: ConcentrationRequest) -> ConcentrationResult:
        """Calcula conversiones con ppm (partes por millón)"""
        result = ConcentrationResult(
            calculation_type=CalculationType.PPM,
            formula_used="ppm = (masa_soluto / masa_solución) × 10⁶"
        )
        
        # Conversiones entre ppm y otras unidades
        if request.ppm is not None:
            result.ppm = request.ppm
            result.percentage = request.ppm / 10000  # ppm a %
            result.concentration_mg_ml = request.ppm / 1000  # ppm a mg/mL (asumiendo densidad ~1)
            
        elif request.percentage is not None:
            result.percentage = request.percentage
            result.ppm = request.percentage * 10000  # % a ppm
            result.concentration_mg_ml = (request.percentage * 10)  # % a mg/mL
            
        elif request.concentration_mg_ml is not None:
            result.concentration_mg_ml = request.concentration_mg_ml
            result.ppm = request.concentration_mg_ml * 1000  # mg/mL a ppm
            result.percentage = result.ppm / 10000  # ppm a %
            
        else:
            raise ConcentrationError("Necesitas especificar ppm, porcentaje o concentración mg/mL")
        
        return result
    
    @classmethod
    def _calculate_percentage(cls, request: ConcentrationRequest) -> ConcentrationResult:
        """Calcula concentraciones porcentuales"""
        result = ConcentrationResult(
            calculation_type=CalculationType.PERCENTAGE,
            formula_used="% = (masa_soluto / masa_solución) × 100"
        )
        
        if request.percentage is not None:
            result.percentage = request.percentage
            result.ppm = request.percentage * 10000
            result.concentration_g_l = request.percentage * 10  # % p/v a g/L
            
        elif request.ppm is not None:
            result.ppm = request.ppm
            result.percentage = request.ppm / 10000
            result.concentration_g_l = result.percentage * 10
            
        else:
            raise ConcentrationError("Necesitas especificar porcentaje o ppm")
        
        return result
    
    @classmethod
    def get_calculation_types(cls):
        """Retorna los tipos de cálculo disponibles."""
        return [
            {"value": CalculationType.MOLARITY.value, "label": "Molaridad (M)"},
            {"value": CalculationType.MOLALITY.value, "label": "Molalidad (m)"},
            {"value": CalculationType.DILUTION.value, "label": "Diluciones (C₁V₁ = C₂V₂)"},
            {"value": CalculationType.MASS_VOLUME.value, "label": "Masa/Volumen (mg/mL, g/L)"},
            {"value": CalculationType.PPM.value, "label": "Partes por millón (ppm)"},
            {"value": CalculationType.PERCENTAGE.value, "label": "Porcentaje (% p/v)"},
        ]