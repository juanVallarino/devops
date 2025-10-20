from app.models import BaseModel
from app import db

class Blacklist(BaseModel):
    __tablename__ = 'blacklists'
    
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    app_uuid = db.Column(db.String(255), nullable=False)
    blocked_reason = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Blacklist {self.email}>'
