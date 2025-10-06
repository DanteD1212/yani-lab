from app import create_app
import os

# Crear la aplicación usando el factory pattern
app = create_app(os.environ.get('FLASK_CONFIG', 'production'))

if __name__ == '__main__':
    # Para desarrollo local
    app.run(debug=app.config['DEBUG'], host='127.0.0.1', port=5000)