import pytest
import tempfile
import os
from app import create_app, db
from app.models.blacklist import Blacklist


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app('testing')
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'WTF_CSRF_ENABLED': False,
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
    
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def auth_headers():
    """Headers with valid token."""
    return {'Authorization': 'Bearer dev-token-123'}


@pytest.fixture
def sample_blacklist_data():
    """Sample data for creating blacklist entries."""
    return {
        'email': 'test@example.com',
        'app_uuid': '123e4567-e89b-12d3-a456-426614174000',
        'blocked_reason': 'Spam detected'
    }


@pytest.fixture
def create_blacklist_entry(app, sample_blacklist_data):
    """Create a blacklist entry in the database."""
    with app.app_context():
        entry = Blacklist(**sample_blacklist_data)
        db.session.add(entry)
        db.session.commit()
        return {'email': entry.email, 'app_uuid': entry.app_uuid, 'blocked_reason': entry.blocked_reason}