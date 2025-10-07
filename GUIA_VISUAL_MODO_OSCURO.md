# 🎨 Guía Visual - Modo Oscuro

## 🖱️ Cómo Activar el Modo Oscuro

### Opción 1: Usando el Botón

```
┌─────────────────────────────────────────────────────────────┐
│  Química Interactiva    Inicio  Conversiones  Neubauer     │
│                         Concentraciones                      │
│                                         ┌──────────────────┐│
│                                         │ ☀️ Modo Oscuro   ││ ← Haz clic aquí
│                                         └──────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### Opción 2: Atajo de Teclado

- **Windows/Linux**: `Ctrl` + `Shift` + `D`
- **Mac**: `Cmd` + `Shift` + `D`

---

## 🎨 Comparación Visual

### MODO CLARO ☀️

```
┌───────────────────────────────────────────┐
│ 🔵 Navbar: Azul Oscuro (#2c3e50)        │
├───────────────────────────────────────────┤
│                                           │
│  📄 Fondo: Gris Claro (#f8f9fa)          │
│                                           │
│  ┌─────────────────────────────────┐     │
│  │ Tarjeta: Blanco (#ffffff)       │     │
│  │                                  │     │
│  │ Texto: Negro Suave (#333333)    │     │
│  └─────────────────────────────────┘     │
│                                           │
└───────────────────────────────────────────┘
│ 🔵 Footer: Azul Oscuro (#2c3e50)        │
└───────────────────────────────────────────┘
```

### MODO OSCURO 🌙

```
┌───────────────────────────────────────────┐
│ ⚫ Navbar: Negro Profundo (#0d1117)      │
├───────────────────────────────────────────┤
│                                           │
│  🌑 Fondo: Negro Azulado (#0f1419)       │
│                                           │
│  ┌─────────────────────────────────┐     │
│  │ Tarjeta: Gris Oscuro (#1e2530)  │     │
│  │                                  │     │
│  │ Texto: Blanco Suave (#e4e7eb)   │     │
│  └─────────────────────────────────┘     │
│                                           │
└───────────────────────────────────────────┘
│ ⚫ Footer: Negro Profundo (#0d1117)      │
└───────────────────────────────────────────┘
```

---

## 🎯 Elementos que Cambian

### ✅ Navegación

- Fondo navbar: Azul oscuro → Negro profundo
- Links: Mantienen visibilidad óptima

### ✅ Contenido Principal

- Fondo: Gris claro → Negro azulado
- Texto: Negro → Blanco suave
- Tarjetas: Blanco → Gris oscuro

### ✅ Formularios

- Inputs: Fondo blanco → Gris oscuro
- Bordes: Gris claro → Gris medio
- Texto: Negro → Blanco

### ✅ Botones

- Primarios: Azul claro → Azul brillante
- Secundarios: Gris → Gris oscuro
- Hover: Efectos adaptados

### ✅ Resultados

- Éxito: Verde claro → Verde oscuro
- Error: Rojo claro → Rojo oscuro
- Info: Azul claro → Azul oscuro

---

## 🌈 Paleta de Colores Completa

### Modo Claro ☀️

| Elemento            | Color          | Hexadecimal |
| ------------------- | -------------- | ----------- |
| 🎨 Fondo principal  | Gris muy claro | `#f8f9fa`   |
| 📄 Fondo tarjetas   | Blanco         | `#ffffff`   |
| 🔵 Navbar/Footer    | Azul oscuro    | `#2c3e50`   |
| ✏️ Texto principal  | Negro suave    | `#333333`   |
| 📝 Texto secundario | Gris medio     | `#666666`   |
| 🔗 Enlaces          | Azul           | `#3498db`   |
| 🎯 Botón primario   | Azul brillante | `#3498db`   |
| ✅ Éxito            | Verde claro    | `#d4edda`   |
| ❌ Error            | Rojo claro     | `#f8d7da`   |

### Modo Oscuro 🌙

| Elemento            | Color          | Hexadecimal |
| ------------------- | -------------- | ----------- |
| 🎨 Fondo principal  | Negro azulado  | `#0f1419`   |
| 📄 Fondo tarjetas   | Gris oscuro    | `#1e2530`   |
| ⚫ Navbar/Footer    | Negro profundo | `#0d1117`   |
| ✏️ Texto principal  | Blanco suave   | `#e4e7eb`   |
| 📝 Texto secundario | Gris claro     | `#a0aec0`   |
| 🔗 Enlaces          | Azul claro     | `#63b3ed`   |
| 🎯 Botón primario   | Azul vibrante  | `#4299e1`   |
| ✅ Éxito            | Verde oscuro   | `#1e3a2e`   |
| ❌ Error            | Rojo oscuro    | `#3a1e1e`   |

---

## 📱 Diseño Responsive

### Desktop (> 768px)

```
┌──────────────────────────────────────────────────────────────┐
│ Química Interactiva    Inicio  Conversiones  Neubauer       │
│                  Concentraciones          [☀️ Modo Oscuro]   │
└──────────────────────────────────────────────────────────────┘
```

### Tablet/Mobile (< 768px)

```
┌─────────────────────────────┐
│   Química Interactiva       │
├─────────────────────────────┤
│        Inicio               │
│      Conversiones           │
│        Neubauer             │
│     Concentraciones         │
├─────────────────────────────┤
│   [☀️ Modo Oscuro]          │
└─────────────────────────────┘
```

---

## ⚡ Transiciones

Todos los cambios son **suaves y animados**:

```
Duración: 400ms
Easing: cubic-bezier(0.4, 0, 0.2, 1)
Propiedades: background-color, color, border-color, box-shadow
```

---

## 🎬 Animaciones

### Al hacer clic en el botón:

```
┌──────────────┐       ┌──────────────┐
│ ☀️ Modo     │  →→→  │ 🌙 Modo     │
│   Oscuro     │ 360°  │   Claro      │
└──────────────┘       └──────────────┘
   Rotación completa
```

### Al cambiar de modo:

```
Modo Claro               Modo Oscuro
   ☀️    →  Fade  →         🌙
(blanco)   400ms      (negro azulado)
```

---

## 💡 Tips de Uso

### Para Usuarios:

1. **Primera vez**: El modo se detecta automáticamente de tu sistema
2. **Cambio manual**: Usa el botón o el atajo de teclado
3. **Persistencia**: Tu elección se guarda automáticamente
4. **Todas las páginas**: El modo se aplica en toda la aplicación

### Para Desarrolladores:

1. **Variables CSS**: Todas las personalizaciones usan variables
2. **Transiciones**: Ya configuradas, solo agregar elementos
3. **API JavaScript**: Disponible para integraciones
4. **Eventos**: Puedes escuchar cambios de modo

---

## 🔍 Detalles Técnicos

### Prevención de FOUC (Flash)

```html
<script>
  // Se ejecuta antes de renderizar
  if (localStorage.getItem("darkMode") === "dark") {
    document.documentElement.classList.add("dark-mode");
  }
</script>
```

### Detección del Sistema

```javascript
// Detecta preferencia del SO
window.matchMedia("(prefers-color-scheme: dark)").matches;
```

### Almacenamiento

```javascript
// Guarda en localStorage
localStorage.setItem("darkMode", "dark");
localStorage.setItem("darkMode", "light");
```

---

## ✨ Características Especiales

🎨 **25+ variables CSS** para personalización fácil  
🔄 **Sincronización automática** con el sistema operativo  
💾 **Persistencia** entre sesiones  
⌨️ **Atajo de teclado** para acceso rápido  
♿ **Accesible** con ARIA labels  
📱 **Responsive** en todos los dispositivos  
⚡ **Animaciones suaves** y profesionales  
🎯 **Sin FOUC** (flash de contenido)

---

## 🎉 ¡Disfruta tu nuevo modo oscuro!

Tu aplicación ahora ofrece una experiencia visual moderna y profesional.
El modo oscuro no solo se ve increíble, sino que también cuida la salud
visual de tus usuarios. 👁️✨

**Servidor corriendo en**: http://localhost:5000  
**¡Pruébalo ahora!** 🚀
