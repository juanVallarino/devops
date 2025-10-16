import pytest
import json


class TestPingEndpoint:
    """Test cases for the ping endpoint."""

    @pytest.mark.unit
    def test_ping_success(self, client):
        """Test successful ping request."""
        response = client.get('/ping')
        
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        
        data = json.loads(response.data)
        assert data['message'] == 'pong'

    @pytest.mark.unit
    def test_ping_method_not_allowed(self, client):
        """Test that POST method is not allowed on ping endpoint."""
        response = client.post('/ping')
        assert response.status_code == 405  # Method Not Allowed

    @pytest.mark.unit
    def test_ping_response_time(self, client):
        """Test that ping response is fast."""
        import time
        start_time = time.time()
        response = client.get('/ping')
        end_time = time.time()
        
        assert response.status_code == 200
        assert (end_time - start_time) < 1.0  # Should respond in less than 1 second
