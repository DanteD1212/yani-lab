// JavaScript para la página de Neubauer

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar los campos de cuadrantes al cargar la página
    actualizarCamposCuadrantes();
});

function actualizarCamposCuadrantes() {
    const numCuadrantes = parseInt(document.getElementById("numCuadrantes").value);
    const camposCuadrantesDiv = document.getElementById("camposCuadrantes");
    
    // Limpiar campos existentes
    camposCuadrantesDiv.innerHTML = "";

    // Crear campos para cada cuadrante
    for (let i = 1; i <= numCuadrantes; i++) {
        const quadrantDiv = document.createElement("div");
        quadrantDiv.className = "quadrant-input";
        
        const label = document.createElement("label");
        label.setAttribute("for", `celdasCuadrante${i}`);
        label.textContent = `Células en Cuadrante ${i}:`;
        
        const input = document.createElement("input");
        input.setAttribute("type", "number");
        input.setAttribute("id", `celdasCuadrante${i}`);
        input.setAttribute("name", `celdasCuadrante${i}`);
        input.setAttribute("min", "0");
        input.setAttribute("required", "true");
        input.setAttribute("placeholder", "Ingrese el número de células");
        input.className = "form-input";
        
        // Agregar validación en tiempo real
        input.addEventListener('input', function() {
            validarCampoNumerico(this, `errorCeldas${i}`);
        });
        
        const errorDiv = document.createElement("div");
        errorDiv.setAttribute("id", `errorCeldas${i}`);
        errorDiv.className = "error-message";
        
        quadrantDiv.appendChild(label);
        quadrantDiv.appendChild(input);
        quadrantDiv.appendChild(errorDiv);
        camposCuadrantesDiv.appendChild(quadrantDiv);
    }
}

function validarCampoNumerico(input, errorDivId) {
    const errorDiv = document.getElementById(errorDivId);
    const valor = parseFloat(input.value);
    
    if (input.value === '') {
        errorDiv.textContent = '';
        return true;
    }
    
    if (isNaN(valor) || valor < 0) {
        errorDiv.textContent = 'Debe ser un número mayor o igual a cero';
        input.classList.add('error');
        return false;
    }
    
    errorDiv.textContent = '';
    input.classList.remove('error');
    return true;
}

function validarFormulario() {
    let valido = true;
    const errores = [];
    
    // Validar volumen del cuadrante
    const volumenCuadrante = parseFloat(document.getElementById("volumenCuadrante").value);
    if (isNaN(volumenCuadrante) || volumenCuadrante <= 0) {
        errores.push('El volumen del cuadrante debe ser un número mayor que cero');
        valido = false;
    }

    // Validar factor de dilución
    const factorDilucion = parseFloat(document.getElementById("factorDilucion").value);
    if (isNaN(factorDilucion) || factorDilucion <= 0) {
        errores.push('El factor de dilución debe ser un número mayor que cero');
        valido = false;
    }

    // Validar número de células en cada cuadrante
    const numCuadrantes = parseInt(document.getElementById("numCuadrantes").value);
    for (let i = 1; i <= numCuadrantes; i++) {
        const celdasInput = document.getElementById(`celdasCuadrante${i}`);
        const celdas = parseInt(celdasInput.value);
        
        if (celdasInput.value === '' || isNaN(celdas) || celdas < 0) {
            errores.push(`El número de células del cuadrante ${i} debe ser un número mayor o igual a cero`);
            valido = false;
        }
    }

    // Mostrar errores si los hay
    if (!valido) {
        alert('Por favor, corrija los siguientes errores:\n\n' + errores.join('\n'));
    }

    return valido;
}

// Agregar validación en tiempo real para todos los campos numéricos
document.addEventListener('DOMContentLoaded', function() {
    const volumenInput = document.getElementById('volumenCuadrante');
    const dilucionInput = document.getElementById('factorDilucion');
    
    volumenInput.addEventListener('input', function() {
        const valor = parseFloat(this.value);
        if (this.value !== '' && (isNaN(valor) || valor <= 0)) {
            this.classList.add('error');
        } else {
            this.classList.remove('error');
        }
    });
    
    dilucionInput.addEventListener('input', function() {
        const valor = parseFloat(this.value);
        if (this.value !== '' && (isNaN(valor) || valor <= 0)) {
            this.classList.add('error');
        } else {
            this.classList.remove('error');
        }
    });
    
    // Agregar validación al formulario
    const form = document.getElementById('neubauerForm');
    if (form) {
        form.addEventListener('submit', function(event) {
            if (!validarFormulario()) {
                event.preventDefault();
            }
        });
    }
});

// Función para limpiar el formulario
function limpiarFormulario() {
    // Restablecer valores por defecto
    document.getElementById('numCuadrantes').value = '4';
    document.getElementById('volumenCuadrante').value = '0.1';
    document.getElementById('factorDilucion').value = '1';
    
    // Actualizar campos de cuadrantes
    actualizarCamposCuadrantes();
    
    // Limpiar cualquier mensaje de error
    document.querySelectorAll('.error-message').forEach(function(errorDiv) {
        errorDiv.textContent = '';
    });
    
    // Remover clases de error
    document.querySelectorAll('.error').forEach(function(element) {
        element.classList.remove('error');
    });
}

// CSS adicional para campos con error
const style = document.createElement('style');
style.textContent = `
    .form-input.error {
        border-color: #dc3545;
        box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.1);
    }
`;
document.head.appendChild(style);