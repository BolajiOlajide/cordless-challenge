from app import create_app
import config


if __name__ == "__main__":
    app = create_app()
    # I modeled a real life production system here, so I set the host to 0.0.0.0
    app.run(host="0.0.0.0", port=8080, debug=config.DEBUG)
