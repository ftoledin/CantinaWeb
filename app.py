from flask import Flask
from config.app_config import configure_app

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Configurar aplicação
    configure_app(app)
    
    @app.route('/')
    def index():
        return "<h1>Cantina FuraFila - Sistema em Desenvolvimento</h1>"
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)