from functools import wraps
from flask import request, jsonify

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({'error': 'Token de autorización requerido'}), 401
            
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Formato de token inválido'}), 401
            
        token = auth_header.split(' ')[1]
        
        if token != 'dev-token-123':
            return jsonify({'error': 'Token inválido'}), 401
            
        return f(*args, **kwargs)
    return decorated_function
