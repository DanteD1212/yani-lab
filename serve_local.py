# Script para desarrollo local en Windows
# Usa waitress en lugar de gunicorn (que no es compatible con Windows)

from waitress import serve
from run import app
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"🚀 Iniciando servidor de desarrollo en http://localhost:{port}")
    print("💡 Usando waitress (compatible con Windows)")
    print("⚠️  En producción (Render) se usará gunicorn automáticamente")
    serve(app, host='0.0.0.0', port=port)