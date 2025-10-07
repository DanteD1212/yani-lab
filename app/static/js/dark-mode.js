// Controlador de modo oscuro
(function() {
    'use strict';

    // Clase para manejar el modo oscuro
    class DarkModeManager {
        constructor() {
            this.darkModeKey = 'darkMode';
            this.body = document.body;
            this.init();
        }

        // Inicializar el modo oscuro
        init() {
            // Cargar preferencia guardada o usar preferencia del sistema
            const savedMode = this.getSavedMode();
            const systemPrefersDark = this.getSystemPreference();
            
            // Si hay una preferencia guardada, usarla; si no, usar la del sistema
            if (savedMode !== null) {
                this.setMode(savedMode === 'dark');
            } else if (systemPrefersDark) {
                this.setMode(true);
            }

            // Escuchar cambios en la preferencia del sistema
            this.watchSystemPreference();
        }

        // Obtener modo guardado en localStorage
        getSavedMode() {
            const saved = localStorage.getItem(this.darkModeKey);
            return saved;
        }

        // Guardar modo en localStorage
        saveMode(isDark) {
            localStorage.setItem(this.darkModeKey, isDark ? 'dark' : 'light');
        }

        // Obtener preferencia del sistema
        getSystemPreference() {
            return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        }

        // Observar cambios en la preferencia del sistema
        watchSystemPreference() {
            if (window.matchMedia) {
                const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
                
                // Para navegadores modernos
                if (mediaQuery.addEventListener) {
                    mediaQuery.addEventListener('change', (e) => {
                        // Solo aplicar si el usuario no ha guardado una preferencia manual
                        if (this.getSavedMode() === null) {
                            this.setMode(e.matches);
                        }
                    });
                } else if (mediaQuery.addListener) {
                    // Para navegadores antiguos
                    mediaQuery.addListener((e) => {
                        if (this.getSavedMode() === null) {
                            this.setMode(e.matches);
                        }
                    });
                }
            }
        }

        // Establecer modo (oscuro o claro)
        setMode(isDark) {
            // Agregar clase de transición
            this.body.classList.add('dark-mode-transition');
            
            if (isDark) {
                this.body.classList.add('dark-mode');
            } else {
                this.body.classList.remove('dark-mode');
            }

            // Actualizar el botón si existe
            this.updateToggleButton(isDark);

            // Remover clase de transición después de completar
            setTimeout(() => {
                this.body.classList.remove('dark-mode-transition');
            }, 400);

            // Disparar evento personalizado
            this.dispatchModeChangeEvent(isDark);
        }

        // Alternar entre modo oscuro y claro
        toggle() {
            const isDark = !this.body.classList.contains('dark-mode');
            this.setMode(isDark);
            this.saveMode(isDark);
            
            // Animación del botón
            this.animateToggle();
        }

        // Actualizar el botón de cambio
        updateToggleButton(isDark) {
            const button = document.getElementById('darkModeToggle');
            if (!button) return;

            const textSpan = button.querySelector('.toggle-text');
            if (textSpan) {
                textSpan.textContent = isDark ? 'Modo Claro' : 'Modo Oscuro';
            }

            // Actualizar aria-label para accesibilidad
            button.setAttribute('aria-label', 
                isDark ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro'
            );
            button.setAttribute('aria-pressed', isDark);
        }

        // Animación del botón al hacer clic
        animateToggle() {
            const button = document.getElementById('darkModeToggle');
            if (!button) return;

            button.style.transform = 'rotate(360deg)';
            setTimeout(() => {
                button.style.transform = '';
            }, 400);
        }

        // Disparar evento personalizado cuando cambia el modo
        dispatchModeChangeEvent(isDark) {
            const event = new CustomEvent('darkModeChange', {
                detail: { isDark }
            });
            window.dispatchEvent(event);
        }

        // Obtener el estado actual
        isDarkMode() {
            return this.body.classList.contains('dark-mode');
        }

        // Método público para que otros scripts escuchen cambios
        onChange(callback) {
            window.addEventListener('darkModeChange', (e) => {
                callback(e.detail.isDark);
            });
        }
    }

    // Crear instancia global
    const darkModeManager = new DarkModeManager();

    // Exponer globalmente para uso en otros scripts
    window.darkModeManager = darkModeManager;

    // Inicializar el botón de cambio cuando el DOM esté listo
    document.addEventListener('DOMContentLoaded', function() {
        const toggleButton = document.getElementById('darkModeToggle');
        
        if (toggleButton) {
            toggleButton.addEventListener('click', function() {
                darkModeManager.toggle();
            });

            // Actualizar el botón al cargar
            darkModeManager.updateToggleButton(darkModeManager.isDarkMode());
        }

        // Agregar atajo de teclado (Ctrl/Cmd + Shift + D)
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'D') {
                e.preventDefault();
                darkModeManager.toggle();
            }
        });
    });

    // Prevenir flash de contenido no estilizado (FOUC)
    // Aplicar modo antes de que se renderice la página
    (function preventFOUC() {
        const savedMode = localStorage.getItem('darkMode');
        if (savedMode === 'dark') {
            document.documentElement.classList.add('dark-mode');
        }
    })();

})();

// Utilidades adicionales para modo oscuro

// Función para obtener el estado actual del modo oscuro
function isDarkMode() {
    return document.body.classList.contains('dark-mode');
}

// Función para forzar modo oscuro
function enableDarkMode() {
    if (window.darkModeManager) {
        window.darkModeManager.setMode(true);
        window.darkModeManager.saveMode(true);
    }
}

// Función para forzar modo claro
function enableLightMode() {
    if (window.darkModeManager) {
        window.darkModeManager.setMode(false);
        window.darkModeManager.saveMode(false);
    }
}

// Función para resetear a preferencia del sistema
function resetToSystemPreference() {
    localStorage.removeItem('darkMode');
    const systemPrefersDark = window.matchMedia && 
        window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (window.darkModeManager) {
        window.darkModeManager.setMode(systemPrefersDark);
    }
}

// Efecto de transición suave para gráficos (opcional)
window.addEventListener('darkModeChange', function(e) {
    // Aquí puedes agregar lógica adicional cuando cambie el modo
    // Por ejemplo, actualizar gráficos, recargar imágenes, etc.
    
    console.log('Modo oscuro:', e.detail.isDark ? 'activado' : 'desactivado');
    
    // Ejemplo: actualizar meta theme-color para navegadores móviles
    updateThemeColor(e.detail.isDark);
});

// Actualizar color del tema en navegadores móviles
function updateThemeColor(isDark) {
    let themeColorMeta = document.querySelector('meta[name="theme-color"]');
    
    if (!themeColorMeta) {
        themeColorMeta = document.createElement('meta');
        themeColorMeta.name = 'theme-color';
        document.head.appendChild(themeColorMeta);
    }
    
    themeColorMeta.content = isDark ? '#0d1117' : '#2c3e50';
}

// Analytics (opcional) - registrar cuando los usuarios cambian el modo
window.addEventListener('darkModeChange', function(e) {
    // Si usas Google Analytics, puedes registrar el evento
    if (typeof gtag !== 'undefined') {
        gtag('event', 'dark_mode_toggle', {
            'mode': e.detail.isDark ? 'dark' : 'light'
        });
    }
});

// Prevenir FOUC (Flash of Unstyled Content)
(function() {
    const savedMode = localStorage.getItem('darkMode');
    if (savedMode === 'dark') {
        document.documentElement.style.backgroundColor = '#0f1419';
        document.documentElement.style.color = '#e4e7eb';
    }
})();
