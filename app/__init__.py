from flask import Flask

from .config import config

def create_app(config_name='default'):
    """Factory function para crear la aplicación Flask."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Registrar blueprints
    from .routes.main import bp as main_bp
    from .routes.conversions import bp as conversions_bp
    from .routes.neubauer import bp as neubauer_bp
    from .routes.concentrations import bp as concentrations_bp
    from .routes.ph import bp as ph_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(conversions_bp)
    app.register_blueprint(neubauer_bp)
    app.register_blueprint(concentrations_bp)
    app.register_blueprint(ph_bp)

    return app
