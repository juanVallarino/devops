from flask_restful import Resource, request
from app.models.blacklist import Blacklist
from app.schemas.blacklist import BlacklistSchema, BlacklistResponseSchema
from app.utils.auth import require_auth
from app import db

class BlacklistResource(Resource):
    
    @require_auth
    def post(self):
        schema = BlacklistSchema()
        try:
            data = schema.load(request.json)
        except Exception as e:
            return {'message': 'Datos inválidos', 'error': str(e)}, 400
        
        existing_blacklist = Blacklist.query.filter_by(email=data['email']).first()
        
        if existing_blacklist:
            return {'message': 'El email ya está en la lista negra'}, 409
        
        try:
            blacklist_entry = Blacklist(
                email=data['email'],
                app_uuid=data['app_uuid'],
                blocked_reason=data['blocked_reason']
            )
            
            db.session.add(blacklist_entry)
            db.session.commit()
            
            return {'message': 'Email agregado exitosamente a la lista negra'}, 201
            
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error al agregar email a la lista negra', 'error': str(e)}, 500

class BlacklistEmailResource(Resource):
    
    @require_auth
    def get(self, email):
        blacklist_entry = Blacklist.query.filter_by(email=email).first()
        
        if blacklist_entry:
            return {
                'is_blocked': True,
                'email': blacklist_entry.email,
                'blocked_reason': blacklist_entry.blocked_reason,
                'app_uuid': blacklist_entry.app_uuid
            }, 200
        else:
            return {
                'is_blocked': False,
                'email': email,
                'message': 'Email no encontrado en la lista negra'
            }, 200
