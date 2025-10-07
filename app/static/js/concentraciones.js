// JavaScript para mejorar la experiencia de usuario en la calculadora de concentraciones

document.addEventListener('DOMContentLoaded', function() {
    // Mejorar la validación en tiempo real
    addRealTimeValidation();
    
    // Agregar funcionalidad de limpiar campos específicos
    addClearFieldButtons();
    
    // Inicializar tooltips informativos
    initializeTooltips();
});



function addRealTimeValidation() {
    const inputs = document.querySelectorAll('input[type="number"]');
    
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            validateInput(this);
        });
        
        input.addEventListener('blur', function() {
            validateInput(this);
        });
    });
}

function validateInput(input) {
    const value = parseFloat(input.value);
    
    // Remover clases de validación previas
    input.classList.remove('invalid', 'valid');
    
    if (input.value === '') {
        return; // Campo vacío es válido (opcional)
    }
    
    if (isNaN(value)) {
        input.classList.add('invalid');
        showTooltip(input, 'Debe ser un número válido');
        return;
    }
    
    // Validaciones específicas por campo
    const fieldName = input.name;
    
    if (['volume_l', 'volume_ml', 'molecular_weight', 'kg_solvent'].includes(fieldName) && value <= 0) {
        input.classList.add('invalid');
        showTooltip(input, 'Debe ser mayor a cero');
        return;
    }
    
    if (['c1', 'c2', 'v1', 'v2'].includes(fieldName) && value <= 0) {
        input.classList.add('invalid');
        showTooltip(input, 'Debe ser mayor a cero');
        return;
    }
    
    input.classList.add('valid');
    hideTooltip(input);
}

function showTooltip(element, message) {
    // Remover tooltip existente
    hideTooltip(element);
    
    const tooltip = document.createElement('div');
    tooltip.className = 'validation-tooltip';
    tooltip.textContent = message;
    
    element.parentNode.appendChild(tooltip);
    
    // Posicionar tooltip
    const rect = element.getBoundingClientRect();
    tooltip.style.position = 'absolute';
    tooltip.style.top = (rect.bottom + 5) + 'px';
    tooltip.style.left = rect.left + 'px';
}

function hideTooltip(element) {
    const existingTooltip = element.parentNode.querySelector('.validation-tooltip');
    if (existingTooltip) {
        existingTooltip.remove();
    }
}

function addClearFieldButtons() {
    const fieldGroups = document.querySelectorAll('.calculation-fields');
    
    fieldGroups.forEach(group => {
        const clearButton = document.createElement('button');
        clearButton.type = 'button';
        clearButton.className = 'btn btn-clear-fields';
        clearButton.textContent = '🗑️ Limpiar Campos';
        clearButton.onclick = () => clearFieldGroup(group);
        
        group.appendChild(clearButton);
    });
}

function clearFieldGroup(group) {
    const inputs = group.querySelectorAll('input');
    inputs.forEach(input => {
        input.value = '';
        input.classList.remove('invalid', 'valid');
    });
    
    const tooltips = group.querySelectorAll('.validation-tooltip');
    tooltips.forEach(tooltip => tooltip.remove());
}

// Funciones de utilidad para formato de números
function formatResult(value, decimals = 4) {
    if (typeof value !== 'number') return value;
    return parseFloat(value.toFixed(decimals));
}

// Agregar funcionalidad de copiar resultados
function addCopyFunctionality() {
    const resultItems = document.querySelectorAll('.result-value');
    
    resultItems.forEach(item => {
        item.style.cursor = 'pointer';
        item.title = 'Clic para copiar';
        
        item.addEventListener('click', function() {
            const text = this.textContent.trim();
            navigator.clipboard.writeText(text).then(() => {
                showCopyConfirmation(this);
            }).catch(err => {
                console.error('Error al copiar: ', err);
            });
        });
    });
}

function showCopyConfirmation(element) {
    const originalText = element.textContent;
    element.textContent = '✓ Copiado!';
    element.style.color = '#28a745';
    
    setTimeout(() => {
        element.textContent = originalText;
        element.style.color = '';
    }, 1500);
}

function clearForm() {
    // Limpiar el formulario completo
    const form = document.querySelector('.concentration-form');
    form.reset();
    
    // Limpiar manualmente todos los inputs numéricos
    const inputs = form.querySelectorAll('input[type="number"]');
    inputs.forEach(input => {
        input.value = '';
        input.classList.remove('invalid', 'valid');
    });
    
    // Limpiar todos los tooltips
    const tooltips = form.querySelectorAll('.validation-tooltip');
    tooltips.forEach(tooltip => tooltip.remove());
    
    // Resetear el dropdown
    const dropdown = document.getElementById('calculation_type');
    dropdown.selectedIndex = 0;
    
    showCalculationFields();
}

// Ejecutar cuando se muestran resultados
document.addEventListener('DOMContentLoaded', function() {
    // Observer para detectar cuando aparecen resultados
    const resultSection = document.querySelector('.result-section');
    if (resultSection) {
        addCopyFunctionality();
    }
});

// Funciones para tooltips informativos
function initializeTooltips() {
    // Crear tooltips para iconos informativos
    createTooltipElements();
    
    // Agregar event listeners para mostrar/ocultar tooltips
    addTooltipEventListeners();
}

function createTooltipElements() {
    const tooltipIcons = document.querySelectorAll('.tooltip-icon');
    const inputsWithTooltips = document.querySelectorAll('input[data-tooltip]');
    
    tooltipIcons.forEach(icon => {
        createTooltipForElement(icon, icon.getAttribute('data-tooltip'));
    });
    
    inputsWithTooltips.forEach(input => {
        createTooltipForElement(input, input.getAttribute('data-tooltip'));
    });
}

function createTooltipForElement(element, tooltipText) {
    if (!tooltipText) return;
    
    // Crear el contenedor del tooltip si no existe
    if (!element.parentNode.classList.contains('tooltip-container')) {
        const container = document.createElement('div');
        container.className = 'tooltip-container';
        container.style.display = 'inline-block';
        
        element.parentNode.insertBefore(container, element);
        container.appendChild(element);
    }
    
    // Crear el elemento del tooltip
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip-text';
    tooltip.textContent = tooltipText;
    
    element.parentNode.appendChild(tooltip);
}

function addTooltipEventListeners() {
    const tooltipContainers = document.querySelectorAll('.tooltip-container');
    
    tooltipContainers.forEach(container => {
        const tooltip = container.querySelector('.tooltip-text');
        if (!tooltip) return;
        
        // Mostrar tooltip en hover
        container.addEventListener('mouseenter', () => {
            showTooltipElement(tooltip);
        });
        
        // Ocultar tooltip cuando se sale el mouse
        container.addEventListener('mouseleave', () => {
            hideTooltipElement(tooltip);
        });
        
        // Para dispositivos táctiles
        container.addEventListener('touchstart', (e) => {
            showTooltipElement(tooltip);
            e.preventDefault();
        });
        
        container.addEventListener('touchend', () => {
            setTimeout(() => hideTooltipElement(tooltip), 2000);
        });
    });
    
    // Tooltips para inputs (mostrar en focus)
    const inputsWithTooltips = document.querySelectorAll('input[data-tooltip]');
    inputsWithTooltips.forEach(input => {
        input.addEventListener('focus', () => {
            const container = input.closest('.tooltip-container');
            if (container) {
                const tooltip = container.querySelector('.tooltip-text');
                if (tooltip) showTooltipElement(tooltip);
            }
        });
        
        input.addEventListener('blur', () => {
            const container = input.closest('.tooltip-container');
            if (container) {
                const tooltip = container.querySelector('.tooltip-text');
                if (tooltip) hideTooltipElement(tooltip);
            }
        });
    });
}

function showTooltipElement(tooltip) {
    tooltip.style.visibility = 'visible';
    tooltip.style.opacity = '1';
    
    // Ajustar posición si se sale de la pantalla
    adjustTooltipPosition(tooltip);
}

function hideTooltipElement(tooltip) {
    tooltip.style.visibility = 'hidden';
    tooltip.style.opacity = '0';
}

function adjustTooltipPosition(tooltip) {
    const rect = tooltip.getBoundingClientRect();
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;
    
    // Ajustar horizontalmente si se sale de la pantalla
    if (rect.right > windowWidth) {
        tooltip.style.left = 'auto';
        tooltip.style.right = '0';
        tooltip.style.marginLeft = '0';
        tooltip.style.marginRight = '10px';
    } else if (rect.left < 0) {
        tooltip.style.left = '0';
        tooltip.style.marginLeft = '10px';
    }
    
    // Ajustar verticalmente si se sale de la pantalla
    if (rect.top < 0) {
        tooltip.style.bottom = 'auto';
        tooltip.style.top = '125%';
        
        // Cambiar la dirección de la flecha
        tooltip.style.setProperty('--arrow-direction', 'bottom');
    }
}

// Función para actualizar tooltips dinámicamente
function updateTooltip(element, newText) {
    const container = element.closest('.tooltip-container');
    if (container) {
        const tooltip = container.querySelector('.tooltip-text');
        if (tooltip) {
            tooltip.textContent = newText;
        }
    }
}

// Función para agregar tooltip a elemento existente
function addTooltipToElement(element, tooltipText) {
    element.setAttribute('data-tooltip', tooltipText);
    createTooltipForElement(element, tooltipText);
    
    // Re-inicializar event listeners para este elemento
    const container = element.closest('.tooltip-container');
    if (container) {
        const tooltip = container.querySelector('.tooltip-text');
        if (tooltip) {
            container.addEventListener('mouseenter', () => showTooltipElement(tooltip));
            container.addEventListener('mouseleave', () => hideTooltipElement(tooltip));
        }
    }
}