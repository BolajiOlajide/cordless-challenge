from flask import Flask


app = Flask(__name__)

app.config.from_object("config")

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return "Not found!", 404
