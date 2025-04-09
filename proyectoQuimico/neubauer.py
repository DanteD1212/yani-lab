class Neubauer:
    @staticmethod
    def calcular_neubauer(num_cuadrantes: int, volumen_cuadrante: float, factor_dilucion: float, celdas: list[int]) -> float:
        """
        Calcula la concentración celular utilizando la fórmula de Neubauer.

        Args:
            num_cuadrantes: El número de cuadrantes contados.
            volumen_cuadrante: El volumen de cada cuadrante contado en mm³.
            factor_dilucion: El factor de dilución aplicado a la muestra.
            celdas: Una lista con el número de células contadas en cada cuadrante.

        Returns:
            La concentración de células en células/mL.
        """
        total_celdas = sum(celdas)
        volumen_total_contado = num_cuadrantes * volumen_cuadrante
        promedio_celdas = total_celdas / num_cuadrantes
        concentracion_celdas_mm3 = promedio_celdas / volumen_total_contado
        concentracion_celdas_mL = concentracion_celdas_mm3 * 1000 * factor_dilucion
        return concentracion_celdas_mL