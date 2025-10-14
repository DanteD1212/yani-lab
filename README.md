# Química Interactiva 🧪

Una aplicación web desarrollada en Flask para ayudar a químicos y bioquímicos con cálculos rápidos y precisos en el laboratorio.

## 🎯 Motivación

Este proyecto tiene dos motivaciones principales:

1. **Ayudar a estudiantes y profesionales** de Bioquímica Diagnóstica con cálculos que se realizan frecuentemente en el laboratorio, haciendo el proceso más eficiente y menos propenso a errores.
2. **Aprender y demostrar** el desarrollo de aplicaciones web usando Python, Flask, HTML, JavaScript y CSS con una arquitectura limpia y escalable.

## ✨ Características

- **Conversiones de Unidades**: Conversión rápida entre diferentes unidades de masa, temperatura y volumen
- **Cálculo de Neubauer**: Cálculo preciso de concentración celular usando cámara de Neubauer
- **Calculadora de pH**: Determinación rápida de pH/pOH para ácidos y bases fuertes
- **Interfaz Intuitiva**: Diseño responsive y fácil de usar
- **Validación de Datos**: Validación en tiempo real para evitar errores
- **Arquitectura Escalable**: Código organizado y modular para fácil mantenimiento

## 🏗️ Arquitectura

El proyecto sigue una arquitectura MVC (Model-View-Controller) con separación clara de responsabilidades:

```
app/
├── models/          # Modelos de datos (ConversionRequest, NeubauerRequest, etc.)
├── services/        # Lógica de negocio (ConversionService, NeubauerService)
├── routes/          # Controladores/Rutas (main, conversions, neubauer)
├── templates/       # Vistas HTML
├── static/          # Archivos estáticos (CSS, JS)
└── utils/           # Utilidades y validadores
```

## 🚀 Instalación y Uso

### Prerrequisitos

- Python 3.8 o superior
- pip

### Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/DanteD1212/proyectoQuimico.git
   cd proyectoQuimico
   ```

2. **Crear entorno virtual** (recomendado):

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:

   ```bash
   # Para desarrollo (Flask development server)
   python run.py

   # Para simular producción localmente (Windows)
   python serve_local.py
   ```

5. **Abrir en el navegador**:
   ```
   http://127.0.0.1:5000  # Flask development server
   http://127.0.0.1:8000  # serve_local.py (waitress)
   ```

## 🧪 Funcionalidades

### Conversiones de Unidades

- **Masa**: Gramos ↔ Kilogramos
- **Temperatura**: Celsius ↔ Fahrenheit
- **Volumen**: Litros ↔ Mililitros

### Cálculo de Neubauer

- Cálculo de concentración celular
- Soporte para 1-5 cuadrantes
- Factor de dilución configurable
- Validación de entrada en tiempo real

### Calculadora de pH

- Estima pH y pOH de ácidos y bases fuertes
- Permite ajustar equivalentes liberados por mol
- Admite modificar la constante iónica del agua para otras temperaturas
- Ofrece notas cuando la solución es demasiado diluida

## ☁️ Despliegue en Render

La aplicación está configurada para desplegarse fácilmente en Render (servicio gratuito):

### Configuración Automática

El repositorio incluye los archivos necesarios para Render:

- `Procfile`: Especifica cómo ejecutar la aplicación (`web: gunicorn run:app`)
- `runtime.txt`: Especifica la versión de Python (`python-3.11.0`)
- `requirements.txt`: Lista todas las dependencias

### Pasos para Desplegar

1. **Conectar Repositorio**:

   - Ve a [Render.com](https://render.com)
   - Conecta tu repositorio de GitHub
   - Selecciona "Web Service"

2. **Configuración en Render**:

   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app`
   - **Environment**: `Python 3`

3. **Variables de Entorno** (opcional):

   - `SECRET_KEY`: Tu clave secreta para producción
   - `FLASK_CONFIG`: `production`

4. **Deploy**: Render detectará automáticamente los cambios y desplegará

### URL de Ejemplo

Una vez desplegada, tu aplicación estará disponible en:
`https://tu-app-name.onrender.com`

## 🧪 Pruebas

Ejecutar las pruebas unitarias:

```bash
python -m unittest discover tests
```

O con pytest:

```bash
pytest tests/
```

## 🛠️ Desarrollo

### Agregar Nueva Funcionalidad

1. **Crear modelo** en `app/models/`
2. **Implementar servicio** en `app/services/`
3. **Crear ruta** en `app/routes/`
4. **Diseñar template** en `app/templates/`
5. **Añadir estilos** en `app/static/css/`
6. **Registrar blueprint** en `app/__init__.py`

### Estructura de Archivos

- `app/models/`: Definiciones de datos y excepciones
- `app/services/`: Lógica de negocio
- `app/routes/`: Rutas y controladores Flask
- `app/templates/`: Plantillas HTML con Jinja2
- `app/static/`: CSS, JavaScript e imágenes
- `tests/`: Pruebas unitarias

## 📁 Migración desde Versión Anterior

Si estás actualizando desde la versión anterior, la nueva estructura mantiene toda la funcionalidad existente pero con mejor organización:

- ✅ Todas las conversiones funcionan igual
- ✅ Cálculos de Neubauer mantienen precisión
- ✅ Interfaz mejorada y más responsive
- ✅ Mejor manejo de errores
- ✅ Código más mantenible

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras este proyecto útil y quieres mejorarlo:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es código abierto. Si usas este código, me encantaría saber cómo te fue útil 😊

## 👨‍💻 Autor

**Dante Daniel** - [GitHub](https://github.com/DanteD1212)

---

_Desarrollado con ❤️ para la comunidad científica_
