# 🌙 Modo Oscuro - Documentación

## Descripción General

Se ha implementado un sistema completo de **modo oscuro** para la aplicación Química Interactiva. Este modo ofrece una experiencia visual optimizada para trabajar en condiciones de poca luz, reduce la fatiga ocular y se adapta automáticamente a las preferencias del sistema operativo del usuario.

## 🎨 Características Principales

### 1. **Cambio Automático según Preferencias del Sistema**

- Detecta automáticamente si el usuario tiene activado el modo oscuro en su sistema operativo
- Se aplica al cargar la página sin necesidad de configuración manual

### 2. **Persistencia de Preferencias**

- Guarda la preferencia del usuario en `localStorage`
- La elección se mantiene entre sesiones y al recargar la página

### 3. **Transiciones Suaves**

- Animaciones fluidas al cambiar entre modos
- Transición de 400ms con curva de easing suave

### 4. **Botón de Alternancia**

- Ubicado en la barra de navegación
- Iconos visuales: ☀️ (sol) para modo claro, 🌙 (luna) para modo oscuro
- Texto descriptivo que cambia según el modo activo

### 5. **Atajo de Teclado**

- **Ctrl + Shift + D** (Windows/Linux)
- **Cmd + Shift + D** (Mac)
- Permite cambiar rápidamente sin usar el ratón

### 6. **Accesibilidad**

- Atributos ARIA para lectores de pantalla
- Contraste optimizado en ambos modos
- Indicadores visuales claros del estado actual

## 📁 Archivos Implementados

### 1. `dark-mode.css`

Contiene todas las variables CSS y estilos para el modo oscuro:

```css
/* Variables para ambos modos */
:root {
  --bg-primary: #f8f9fa;
  --text-primary: #333333;
  /* ... más variables */
}

body.dark-mode {
  --bg-primary: #0f1419;
  --text-primary: #e4e7eb;
  /* ... más variables */
}
```

**Variables principales:**

- **Fondos**: `--bg-primary`, `--bg-secondary`, `--bg-card`
- **Textos**: `--text-primary`, `--text-secondary`, `--text-navbar`
- **Bordes**: `--border-color`, `--border-light`
- **Botones**: `--btn-primary`, `--btn-secondary`
- **Estados**: `--success-bg`, `--error-bg`, `--info-bg`

### 2. `dark-mode.js`

Controlador JavaScript que gestiona la funcionalidad del modo oscuro:

**Clase Principal: `DarkModeManager`**

- `init()` - Inicializa el modo oscuro
- `toggle()` - Alterna entre modos
- `setMode(isDark)` - Establece un modo específico
- `getSavedMode()` - Obtiene la preferencia guardada
- `getSystemPreference()` - Detecta la preferencia del sistema

**Funciones Globales:**

```javascript
isDarkMode(); // Retorna true si está en modo oscuro
enableDarkMode(); // Activa el modo oscuro
enableLightMode(); // Activa el modo claro
resetToSystemPreference(); // Resetea a la preferencia del sistema
```

### 3. `base.html` (Actualizado)

Se agregaron:

- Link al archivo `dark-mode.css`
- Script inline para prevenir FOUC (Flash of Unstyled Content)
- Botón de alternancia en el navbar
- Script `dark-mode.js` al final del body

## 🎯 Colores del Modo Oscuro

### Paleta de Colores Oscuros

| Elemento          | Color     | Uso                      |
| ----------------- | --------- | ------------------------ |
| Fondo Principal   | `#0f1419` | Fondo del body           |
| Fondo Secundario  | `#1a1f2e` | Contenedores             |
| Fondo de Tarjetas | `#1e2530` | Cards, formularios       |
| Navbar/Footer     | `#0d1117` | Navegación y pie         |
| Inputs            | `#252d3a` | Campos de entrada        |
| Texto Principal   | `#e4e7eb` | Títulos y texto          |
| Texto Secundario  | `#a0aec0` | Párrafos y descripciones |
| Bordes            | `#2d3748` | Bordes y separadores     |

### Paleta de Colores Claros (Modo Original)

| Elemento         | Color     | Uso                      |
| ---------------- | --------- | ------------------------ |
| Fondo Principal  | `#f8f9fa` | Fondo del body           |
| Fondo Secundario | `#ffffff` | Contenedores             |
| Navbar/Footer    | `#2c3e50` | Navegación y pie         |
| Texto Principal  | `#333333` | Títulos y texto          |
| Texto Secundario | `#666666` | Párrafos y descripciones |

## 🚀 Uso

### Para Usuarios

1. **Cambio Manual:**

   - Hacer clic en el botón "Modo Oscuro/Claro" en la barra de navegación
   - Usar el atajo de teclado: **Ctrl+Shift+D** (Windows/Linux) o **Cmd+Shift+D** (Mac)

2. **Automático:**
   - Si tu sistema operativo tiene activado el modo oscuro, la página lo detectará automáticamente
   - La preferencia se guarda y se mantiene entre sesiones

### Para Desarrolladores

1. **Escuchar cambios de modo:**

```javascript
window.addEventListener("darkModeChange", function (e) {
  console.log("Modo oscuro:", e.detail.isDark);
  // Tu código aquí
});
```

2. **Verificar estado actual:**

```javascript
if (isDarkMode()) {
  // Está en modo oscuro
} else {
  // Está en modo claro
}
```

3. **Forzar un modo:**

```javascript
enableDarkMode(); // Activar modo oscuro
enableLightMode(); // Activar modo claro
```

4. **Agregar estilos personalizados:**

```css
/* En tu archivo CSS */
body.dark-mode .mi-elemento {
  background-color: var(--bg-card);
  color: var(--text-primary);
}
```

## 🔧 Personalización

### Cambiar Colores

Edita las variables en `dark-mode.css`:

```css
body.dark-mode {
  /* Cambia estos valores según tu preferencia */
  --bg-primary: #tu-color-aqui;
  --text-primary: #tu-color-aqui;
}
```

### Agregar Nuevos Elementos

1. Usa las variables CSS existentes:

```css
.nuevo-elemento {
  background-color: var(--bg-card);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
}
```

2. Si necesitas estilos específicos para modo oscuro:

```css
body.dark-mode .nuevo-elemento {
  /* Estilos específicos para modo oscuro */
}
```

## 🎨 Mejores Prácticas

1. **Usa Variables CSS**: Siempre utiliza las variables definidas en lugar de colores hardcodeados
2. **Prueba Ambos Modos**: Asegúrate de que tu contenido sea legible en ambos modos
3. **Contraste Adecuado**: Mantén un ratio de contraste mínimo de 4.5:1 para texto
4. **Transiciones Suaves**: Usa las transiciones definidas para cambios de color
5. **Accesibilidad**: Verifica que todos los elementos interactivos sean visibles y accesibles

## 📱 Responsive Design

El botón de modo oscuro se adapta a diferentes tamaños de pantalla:

- **Desktop**: Botón en la esquina derecha del navbar
- **Tablet/Mobile**: Botón se muestra debajo de los links de navegación
- **Pequeñas pantallas**: Botón con ancho completo y centrado

## 🐛 Troubleshooting

### El modo no cambia

- Verifica que `dark-mode.js` esté cargando correctamente
- Revisa la consola del navegador en busca de errores
- Limpia el localStorage: `localStorage.removeItem('darkMode')`

### Los colores no se aplican

- Asegúrate de que `dark-mode.css` esté incluido después de `base.css`
- Verifica que los elementos usen las variables CSS correctas

### FOUC (Flash of content)

- El script inline en `<head>` debería prevenir esto
- Si persiste, verifica que el script se esté ejecutando

## 🔄 Actualizaciones Futuras Sugeridas

1. **Selector de Temas**: Agregar más opciones de color (ej: azul oscuro, gris oscuro)
2. **Modo Automático**: Cambiar automáticamente según la hora del día
3. **Animaciones Avanzadas**: Transiciones más elaboradas entre modos
4. **Configuración Avanzada**: Panel de ajustes para personalizar colores
5. **Exportar/Importar**: Compartir configuraciones de tema entre dispositivos

## 📊 Estadísticas

- **Líneas de CSS**: ~600 líneas
- **Líneas de JS**: ~300 líneas
- **Variables CSS**: 25+ variables
- **Compatibilidad**: Chrome 76+, Firefox 67+, Safari 12.1+, Edge 79+

## 🎉 Beneficios

1. **Salud Visual**: Reduce la fatiga ocular en condiciones de poca luz
2. **Ahorro de Batería**: En pantallas OLED/AMOLED ahorra hasta 60% de batería
3. **Preferencia del Usuario**: Respeta las preferencias del sistema
4. **Experiencia Moderna**: Característica esperada en aplicaciones web modernas
5. **Accesibilidad**: Mejor para usuarios con sensibilidad a la luz

## 📝 Notas Técnicas

- Usa `localStorage` para persistencia
- Implementa `matchMedia` para detectar preferencias del sistema
- Previene FOUC con script inline
- Transiciones con `cubic-bezier` para suavidad
- Eventos personalizados para extensibilidad

---

**Desarrollado para**: Química Interactiva  
**Autor**: Dante Daniel  
**Fecha**: 2025  
**Versión**: 1.0
