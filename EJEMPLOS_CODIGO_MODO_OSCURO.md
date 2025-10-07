# 👨‍💻 Ejemplos de Código - Modo Oscuro

## 📚 Índice

1. [Uso Básico](#uso-básico)
2. [Agregar Nuevos Elementos](#agregar-nuevos-elementos)
3. [Personalizar Colores](#personalizar-colores)
4. [Integración JavaScript](#integración-javascript)
5. [Responsive Design](#responsive-design)
6. [Solución de Problemas](#solución-de-problemas)

---

## 🎯 Uso Básico

### HTML - Agregar un Nuevo Elemento

```html
<!-- Tarjeta que se adapta automáticamente al modo oscuro -->
<div class="mi-tarjeta">
  <h3>Título de mi tarjeta</h3>
  <p>Contenido que se adapta automáticamente</p>
  <button class="btn btn-primary">Acción</button>
</div>
```

### CSS - Estilizar con Variables

```css
/* En tu archivo CSS personalizado */
.mi-tarjeta {
  /* Usar variables en lugar de colores fijos */
  background-color: var(--bg-card);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: var(--shadow-md);
}

.mi-tarjeta h3 {
  color: var(--text-primary);
  margin-bottom: 1rem;
}

.mi-tarjeta p {
  color: var(--text-secondary);
  line-height: 1.6;
}
```

**✅ Ventaja**: No necesitas escribir código específico para modo oscuro, las variables CSS hacen el trabajo.

---

## 🎨 Agregar Nuevos Elementos

### Ejemplo 1: Card de Información

```html
<div class="info-card">
  <div class="info-header">
    <h4>Información Importante</h4>
  </div>
  <div class="info-body">
    <p>Este contenido se adapta automáticamente al modo oscuro.</p>
  </div>
</div>
```

```css
.info-card {
  background-color: var(--bg-card);
  border-radius: 12px;
  box-shadow: var(--shadow-md);
  overflow: hidden;
  transition: box-shadow 0.3s ease;
}

.info-card:hover {
  box-shadow: var(--shadow-lg);
}

.info-header {
  background-color: var(--bg-secondary);
  padding: 1rem 1.5rem;
  border-bottom: 1px solid var(--border-color);
}

.info-header h4 {
  color: var(--text-primary);
  margin: 0;
}

.info-body {
  padding: 1.5rem;
}

.info-body p {
  color: var(--text-secondary);
  margin: 0;
}
```

### Ejemplo 2: Tabla Adaptable

```html
<table class="data-table">
  <thead>
    <tr>
      <th>Columna 1</th>
      <th>Columna 2</th>
      <th>Columna 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dato 1</td>
      <td>Dato 2</td>
      <td>Dato 3</td>
    </tr>
  </tbody>
</table>
```

```css
.data-table {
  width: 100%;
  background-color: var(--bg-card);
  border-collapse: collapse;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.data-table thead {
  background-color: var(--bg-secondary);
}

.data-table th {
  color: var(--text-primary);
  font-weight: 600;
  padding: 1rem;
  text-align: left;
  border-bottom: 2px solid var(--border-color);
}

.data-table td {
  color: var(--text-secondary);
  padding: 1rem;
  border-bottom: 1px solid var(--border-light);
}

.data-table tbody tr:hover {
  background-color: var(--bg-input);
}

.data-table tbody tr:last-child td {
  border-bottom: none;
}
```

### Ejemplo 3: Alert/Notification

```html
<div class="alert alert-info">
  <span class="alert-icon">ℹ️</span>
  <div class="alert-content">
    <strong>Información:</strong> Este es un mensaje informativo.
  </div>
</div>
```

```css
.alert {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  border-left: 4px solid;
  margin-bottom: 1rem;
}

.alert-info {
  background-color: var(--info-bg);
  border-left-color: var(--info-border);
  color: var(--info-text);
}

.alert-icon {
  font-size: 1.5rem;
}

.alert-content {
  flex: 1;
}

.alert-content strong {
  display: block;
  margin-bottom: 0.25rem;
}
```

---

## 🎨 Personalizar Colores

### Cambiar Colores del Modo Oscuro

```css
/* En dark-mode.css o tu archivo CSS */
body.dark-mode {
  /* Cambiar color de fondo principal */
  --bg-primary: #1a1a2e; /* Tu color personalizado */

  /* Cambiar color de texto */
  --text-primary: #eaeaea;

  /* Cambiar color de acento */
  --btn-primary: #00d4ff;

  /* Cambiar colores de navbar */
  --bg-navbar: #16213e;
}
```

### Crear un Tema Personalizado

```css
/* Tema azul oscuro personalizado */
body.dark-mode.theme-blue {
  --bg-primary: #0a192f;
  --bg-secondary: #112240;
  --bg-card: #172a45;
  --text-primary: #ccd6f6;
  --text-secondary: #8892b0;
  --btn-primary: #64ffda;
}

/* Tema morado personalizado */
body.dark-mode.theme-purple {
  --bg-primary: #1a0e2e;
  --bg-secondary: #2d1b4e;
  --bg-card: #3d2963;
  --text-primary: #e9d5ff;
  --text-secondary: #c4b5fd;
  --btn-primary: #a78bfa;
}
```

```javascript
// Aplicar tema personalizado
function applyTheme(themeName) {
  document.body.classList.add(`theme-${themeName}`);
}

// Uso
applyTheme("blue"); // Aplica tema azul
applyTheme("purple"); // Aplica tema morado
```

---

## 🔧 Integración JavaScript

### Ejemplo 1: Verificar Estado Actual

```javascript
// Verificar si está en modo oscuro
if (isDarkMode()) {
  console.log("Modo oscuro está activado");
  // Tu código aquí
} else {
  console.log("Modo claro está activado");
  // Tu código aquí
}
```

### Ejemplo 2: Escuchar Cambios de Modo

```javascript
// Escuchar cuando cambia el modo
window.addEventListener("darkModeChange", function (event) {
  const isDark = event.detail.isDark;

  if (isDark) {
    console.log("Cambiado a modo oscuro");
    // Actualizar gráficos, imágenes, etc.
    updateChartTheme("dark");
  } else {
    console.log("Cambiado a modo claro");
    updateChartTheme("light");
  }
});

// Función ejemplo para actualizar un gráfico
function updateChartTheme(theme) {
  // Aquí iría tu código para actualizar Chart.js, D3.js, etc.
  if (window.myChart) {
    window.myChart.options.plugins.legend.labels.color =
      theme === "dark" ? "#e4e7eb" : "#333333";
    window.myChart.update();
  }
}
```

### Ejemplo 3: Cambiar Modo Programáticamente

```javascript
// Activar modo oscuro
function activateDarkMode() {
  enableDarkMode();
  console.log("Modo oscuro activado");
}

// Activar modo claro
function activateLightMode() {
  enableLightMode();
  console.log("Modo claro activado");
}

// Toggle (alternar)
function toggleMode() {
  if (window.darkModeManager) {
    window.darkModeManager.toggle();
  }
}

// Usar preferencia del sistema
function useSystemTheme() {
  resetToSystemPreference();
}
```

### Ejemplo 4: Cargar Recursos Según el Modo

```javascript
// Cargar imagen diferente según el modo
function loadThemedImage(lightSrc, darkSrc) {
  const img = document.getElementById("themed-image");
  const isDark = isDarkMode();
  img.src = isDark ? darkSrc : lightSrc;
}

// Uso
loadThemedImage(
  "/static/images/logo-light.png",
  "/static/images/logo-dark.png"
);

// Actualizar cuando cambie el modo
window.addEventListener("darkModeChange", function (e) {
  loadThemedImage(
    "/static/images/logo-light.png",
    "/static/images/logo-dark.png"
  );
});
```

### Ejemplo 5: Integración con Chart.js

```javascript
// Configuración de Chart.js que se adapta al modo
function createChart() {
  const ctx = document.getElementById("myChart").getContext("2d");
  const isDark = isDarkMode();

  const chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Enero", "Febrero", "Marzo"],
      datasets: [
        {
          label: "Ventas",
          data: [12, 19, 3],
          backgroundColor: isDark
            ? "rgba(66, 153, 225, 0.5)"
            : "rgba(52, 152, 219, 0.5)",
          borderColor: isDark
            ? "rgba(66, 153, 225, 1)"
            : "rgba(52, 152, 219, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          labels: {
            color: isDark ? "#e4e7eb" : "#333333",
          },
        },
      },
      scales: {
        y: {
          ticks: {
            color: isDark ? "#a0aec0" : "#666666",
          },
          grid: {
            color: isDark ? "#2d3748" : "#e9ecef",
          },
        },
        x: {
          ticks: {
            color: isDark ? "#a0aec0" : "#666666",
          },
          grid: {
            color: isDark ? "#2d3748" : "#e9ecef",
          },
        },
      },
    },
  });

  // Actualizar cuando cambie el modo
  window.addEventListener("darkModeChange", function (e) {
    updateChartColors(chart, e.detail.isDark);
  });

  return chart;
}

function updateChartColors(chart, isDark) {
  chart.data.datasets[0].backgroundColor = isDark
    ? "rgba(66, 153, 225, 0.5)"
    : "rgba(52, 152, 219, 0.5)";
  chart.data.datasets[0].borderColor = isDark
    ? "rgba(66, 153, 225, 1)"
    : "rgba(52, 152, 219, 1)";

  chart.options.plugins.legend.labels.color = isDark ? "#e4e7eb" : "#333333";
  chart.options.scales.y.ticks.color = isDark ? "#a0aec0" : "#666666";
  chart.options.scales.x.ticks.color = isDark ? "#a0aec0" : "#666666";
  chart.options.scales.y.grid.color = isDark ? "#2d3748" : "#e9ecef";
  chart.options.scales.x.grid.color = isDark ? "#2d3748" : "#e9ecef";

  chart.update();
}
```

---

## 📱 Responsive Design

### Ejemplo: Card Responsive con Modo Oscuro

```html
<div class="responsive-card">
  <h3>Título Responsive</h3>
  <p>Este card se adapta al tamaño de pantalla y al modo oscuro.</p>
</div>
```

```css
.responsive-card {
  background-color: var(--bg-card);
  color: var(--text-primary);
  padding: 2rem;
  border-radius: 12px;
  box-shadow: var(--shadow-md);
  max-width: 100%;
}

/* Tablet */
@media (max-width: 768px) {
  .responsive-card {
    padding: 1.5rem;
    border-radius: 8px;
  }
}

/* Mobile */
@media (max-width: 480px) {
  .responsive-card {
    padding: 1rem;
    border-radius: 6px;
  }
}

/* Modo oscuro específico en mobile */
@media (max-width: 480px) {
  body.dark-mode .responsive-card {
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border-color);
  }
}
```

---

## 🐛 Solución de Problemas

### Problema: Elemento no se Adapta al Modo Oscuro

**Incorrecto** ❌

```css
.mi-elemento {
  background-color: #ffffff; /* Color fijo */
  color: #333333;
}
```

**Correcto** ✅

```css
.mi-elemento {
  background-color: var(--bg-card); /* Variable CSS */
  color: var(--text-primary);
}
```

### Problema: Color Específico Solo en Modo Oscuro

```css
/* Estilo por defecto (modo claro) */
.elemento-especial {
  background-color: var(--bg-card);
  color: var(--text-primary);
}

/* Estilo específico solo para modo oscuro */
body.dark-mode .elemento-especial {
  /* Sobrescribir solo lo necesario */
  background: linear-gradient(135deg, #4a5568 0%, #2d3748 100%);
  border: 1px solid #4299e1;
}
```

### Problema: Imagen no se Ve Bien en Modo Oscuro

```html
<!-- Opción 1: Usar picture element -->
<picture>
  <source
    srcset="/static/images/logo-dark.png"
    media="(prefers-color-scheme: dark)"
  />
  <img src="/static/images/logo-light.png" alt="Logo" />
</picture>

<!-- Opción 2: Aplicar filtro CSS -->
<img src="/static/images/logo.png" alt="Logo" class="adaptive-image" />
```

```css
/* Aplicar filtro solo en modo oscuro */
body.dark-mode .adaptive-image {
  filter: brightness(0.8) contrast(1.2);
}
```

### Problema: FOUC (Flash of Unstyled Content)

```html
<!-- Agregar en <head> ANTES de cargar estilos -->
<script>
  (function () {
    const savedMode = localStorage.getItem("darkMode");
    if (savedMode === "dark") {
      document.documentElement.classList.add("dark-mode");
      // Aplicar estilos básicos inmediatamente
      document.documentElement.style.backgroundColor = "#0f1419";
      document.documentElement.style.color = "#e4e7eb";
    }
  })();
</script>
```

---

## 📊 Variables CSS Disponibles

### Lista Completa de Variables

```css
/* FONDOS */
--bg-primary          /* Fondo principal de la página */
--bg-secondary        /* Fondo secundario / contenedores */
--bg-card             /* Fondo de tarjetas */
--bg-navbar           /* Fondo de la barra de navegación */
--bg-footer           /* Fondo del pie de página */
--bg-input            /* Fondo de campos de entrada */
--bg-gradient-start   /* Inicio del gradiente */
--bg-gradient-end     /* Fin del gradiente */
--bg-result           /* Gradiente para resultados */

/* TEXTOS */
--text-primary        /* Texto principal / títulos */
--text-secondary      /* Texto secundario / párrafos */
--text-navbar         /* Texto en navbar */
--text-light          /* Texto claro / labels */
--text-muted          /* Texto deshabilitado */
--text-link           /* Color de enlaces */

/* BORDES Y SOMBRAS */
--border-color        /* Color de bordes */
--border-light        /* Bordes claros / separadores */
--shadow-sm           /* Sombra pequeña */
--shadow-md           /* Sombra mediana */
--shadow-lg           /* Sombra grande */

/* BOTONES */
--btn-primary         /* Color botón primario */
--btn-primary-hover   /* Hover botón primario */
--btn-secondary       /* Color botón secundario */
--btn-secondary-hover /* Hover botón secundario */

/* ESTADOS */
--success-bg          /* Fondo mensaje de éxito */
--success-border      /* Borde mensaje de éxito */
--success-text        /* Texto mensaje de éxito */
--error-bg            /* Fondo mensaje de error */
--error-border        /* Borde mensaje de error */
--error-text          /* Texto mensaje de error */
--info-bg             /* Fondo mensaje informativo */
--info-border         /* Borde mensaje informativo */
--info-text           /* Texto mensaje informativo */
```

---

## 🎓 Mejores Prácticas

### ✅ DO (Hacer)

1. **Usar variables CSS siempre**

   ```css
   background-color: var(--bg-card);
   color: var(--text-primary);
   ```

2. **Agregar transiciones suaves**

   ```css
   transition: background-color 0.3s ease, color 0.3s ease;
   ```

3. **Mantener contraste adecuado**

   ```css
   /* Asegurar legibilidad */
   color: var(--text-primary); /* Alto contraste */
   ```

4. **Probar en ambos modos**
   - Verificar visualmente en modo claro y oscuro
   - Comprobar contraste y legibilidad

### ❌ DON'T (No hacer)

1. **NO usar colores fijos**

   ```css
   /* ❌ Incorrecto */
   background-color: #ffffff;
   color: #000000;
   ```

2. **NO olvidar transiciones**

   ```css
   /* ❌ Cambio brusco */
   background-color: var(--bg-card);
   /* Sin transition */
   ```

3. **NO asumir que funciona sin probar**
   - Siempre verificar en ambos modos
   - Probar en diferentes dispositivos

---

## 🚀 Código de Inicio Rápido

### Plantilla HTML Completa

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mi Página con Modo Oscuro</title>

    <!-- Prevenir FOUC -->
    <script>
      (function () {
        if (localStorage.getItem("darkMode") === "dark") {
          document.documentElement.classList.add("dark-mode");
        }
      })();
    </script>

    <!-- CSS -->
    <link rel="stylesheet" href="/static/css/base.css" />
    <link rel="stylesheet" href="/static/css/dark-mode.css" />
  </head>
  <body>
    <!-- Tu contenido aquí -->
    <div class="container">
      <h1>Hola Mundo</h1>
      <p>Este contenido se adapta al modo oscuro automáticamente.</p>
      <button class="btn btn-primary">Botón</button>
    </div>

    <!-- JavaScript -->
    <script src="/static/js/dark-mode.js"></script>
  </body>
</html>
```

---

¡Con estos ejemplos, puedes extender y personalizar el modo oscuro fácilmente! 🎉
