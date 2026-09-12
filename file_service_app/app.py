from flask import Flask
from routes.file_routes import file_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(file_bp, url_prefix="/files")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    # addng this comment
app.run == "main"
app.run2  == "main"

