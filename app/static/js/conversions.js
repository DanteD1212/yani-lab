// JavaScript para la página de conversiones

document.addEventListener('DOMContentLoaded', function() {
    const tipoUnidadSelect = document.getElementById('tipo_unidad');
    const unidadOrigenSelect = document.getElementById('unidad_origen');
    const unidadDestinoSelect = document.getElementById('unidad_destino');

    // Definir las unidades disponibles por tipo
    const unidadesPorTipo = {
        masa: ['gramos', 'kilogramos'],
        temperatura: ['celsius', 'fahrenheit'],
        volumen: ['litros', 'mililitros']
    };

    // Función para capitalizar la primera letra
    function capitalizeFirst(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    // Función para actualizar las opciones de unidades
    function actualizarUnidades() {
        const tipoSeleccionado = tipoUnidadSelect.value;

        // Limpiar y deshabilitar los selectores de unidad
        unidadOrigenSelect.innerHTML = '<option value="">Seleccionar unidad</option>';
        unidadDestinoSelect.innerHTML = '<option value="">Seleccionar unidad</option>';
        
        if (tipoSeleccionado && unidadesPorTipo[tipoSeleccionado]) {
            // Habilitar los selectores
            unidadOrigenSelect.disabled = false;
            unidadDestinoSelect.disabled = false;

            // Añadir las opciones de unidades
            const unidades = unidadesPorTipo[tipoSeleccionado];
            unidades.forEach(unidad => {
                // Crear opción para unidad origen
                const optionOrigen = document.createElement('option');
                optionOrigen.value = unidad;
                optionOrigen.textContent = capitalizeFirst(unidad);
                unidadOrigenSelect.appendChild(optionOrigen);

                // Crear opción para unidad destino
                const optionDestino = document.createElement('option');
                optionDestino.value = unidad;
                optionDestino.textContent = capitalizeFirst(unidad);
                unidadDestinoSelect.appendChild(optionDestino);
            });

            // Restaurar valores seleccionados si existen (para mantener el estado después de envío)
            const valorUnidadOrigen = unidadOrigenSelect.getAttribute('data-selected');
            const valorUnidadDestino = unidadDestinoSelect.getAttribute('data-selected');
            
            if (valorUnidadOrigen) {
                unidadOrigenSelect.value = valorUnidadOrigen;
            }
            if (valorUnidadDestino) {
                unidadDestinoSelect.value = valorUnidadDestino;
            }
        } else {
            // Deshabilitar los selectores si no hay tipo seleccionado
            unidadOrigenSelect.disabled = true;
            unidadDestinoSelect.disabled = true;
        }
    }

    // Event listener para cambios en el tipo de unidad
    tipoUnidadSelect.addEventListener('change', actualizarUnidades);

    // Inicializar al cargar la página
    actualizarUnidades();

    // Función para validar el formulario antes del envío
    function validarFormulario(event) {
        const valor = document.getElementById('valor').value;
        const tipoUnidad = tipoUnidadSelect.value;
        const unidadOrigen = unidadOrigenSelect.value;
        const unidadDestino = unidadDestinoSelect.value;

        let errores = [];

        if (!valor || valor.trim() === '') {
            errores.push('El valor a convertir es requerido');
        } else if (isNaN(valor) || parseFloat(valor) < 0) {
            errores.push('El valor debe ser un número válido mayor o igual a cero');
        }

        if (!tipoUnidad) {
            errores.push('Debe seleccionar un tipo de unidad');
        }

        if (!unidadOrigen) {
            errores.push('Debe seleccionar una unidad de origen');
        }

        if (!unidadDestino) {
            errores.push('Debe seleccionar una unidad de destino');
        }

        if (errores.length > 0) {
            event.preventDefault();
            alert('Por favor, corrija los siguientes errores:\n\n' + errores.join('\n'));
            return false;
        }

        return true;
    }

    // Añadir validación al formulario
    const form = document.querySelector('.conversion-form');
    if (form) {
        form.addEventListener('submit', validarFormulario);
    }

    // Función para limpiar el formulario
    function limpiarFormulario() {
        document.getElementById('valor').value = '';
        tipoUnidadSelect.value = '';
        unidadOrigenSelect.value = '';
        unidadDestinoSelect.value = '';
        actualizarUnidades();
    }

    // Añadir botón de limpiar si no existe
    const btnLimpiar = document.getElementById('btn-limpiar');
    if (btnLimpiar) {
        btnLimpiar.addEventListener('click', limpiarFormulario);
    }
});