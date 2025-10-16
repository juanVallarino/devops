class TestBasicFunctionality:
    """Basic test cases for API endpoints."""

    def test_ping_endpoint(self, client):
        """Test ping endpoint works."""
        response = client.get('/ping')
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'pong'

    def test_blacklist_post_with_token(self, client, auth_headers, sample_blacklist_data):
        """Test POST blacklist with valid token."""
        response = client.post(
            '/blacklists',
            headers=auth_headers,
            json=sample_blacklist_data
        )
        assert response.status_code == 201
        data = response.get_json()
        assert 'exitosamente' in data['message']

    def test_blacklist_get_with_token(self, client, auth_headers, create_blacklist_entry):
        """Test GET blacklist with valid token."""
        email = create_blacklist_entry['email']
        response = client.get(
            f'/blacklists/{email}',
            headers=auth_headers
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data['is_blocked'] is True

    def test_blacklist_duplicate_email(self, client, auth_headers, sample_blacklist_data, create_blacklist_entry):
        """Test duplicate email returns 409."""
        response = client.post(
            '/blacklists',
            headers=auth_headers,
            json=sample_blacklist_data
        )
        assert response.status_code == 409

    def test_blacklist_invalid_email(self, client, auth_headers):
        """Test invalid email format returns 400."""
        invalid_data = {
            'email': 'invalid-email',
            'app_uuid': '123e4567-e89b-12d3-a456-426614174000',
            'blocked_reason': 'Test'
        }
        response = client.post(
            '/blacklists',
            headers=auth_headers,
            json=invalid_data
        )
        assert response.status_code == 400

    def test_blacklist_email_not_found(self, client, auth_headers):
        """Test email not in blacklist returns correct response."""
        response = client.get(
            '/blacklists/nonexistent@example.com',
            headers=auth_headers
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data['is_blocked'] is False
