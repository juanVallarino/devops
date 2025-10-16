from app import create_app, db
from app.models.blacklist import Blacklist

def init_db():
    app = create_app()
    
    with app.app_context():
        db.create_all()
        print("Base de datos inicializada correctamente")
        print("Tablas creadas:")
        print("- blacklists")

if __name__ == '__main__':
    init_db()
