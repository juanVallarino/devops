import os
from app import create_app, db

app = create_app(os.getenv('FLASK_ENV', 'development'))

def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos inicializada correctamente")
        print("Tablas creadas:")
        print("- blacklists")

if __name__ == '_main_':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)