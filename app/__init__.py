from flask import Flask

from koii import Koii


koii = Koii()

def create_app():
    app = Flask(__name__)

    app.config.from_object("config")

    from app.modules.ivr import ivr_blueprint
    app.register_blueprint(ivr_blueprint, url_prefix='/ivr')

    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return "Not found!", 404

    koii.init_app(app)

    return app
