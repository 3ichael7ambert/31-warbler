from unittest import TestCase
from models import db, User
from app import app

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# Use test database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///warbler_test'

# Disable CSRF tokens in the forms (only for testing purposes!)
app.config['WTF_CSRF_ENABLED'] = False

class UserViewsTestCase(TestCase):
    """Test views for user-related routes."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        self.client = app.test_client()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_signup_form(self):
        """Can a user sign up?"""

        # Make a POST request to sign up
        response = self.client.post('/signup', data={
            'username': 'testuser',
            'email': 'test@test.com',
            'password': 'test123',
            'image_url': ''
        }, follow_redirects=True)

        # Check that the response contains the signup success message
        self.assertIn(b'You successfully created your account!', response.data)

        # Check that the user was added to the database
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@test.com')

    def test_login_form(self):
        """Can a user login?"""

        # Create a user
        user = User.signup(username='testuser', email='test@test.com', password='test123', image_url=None)
        db.session.commit()

        # Make a POST request to login
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'test123'
        }, follow_redirects=True)

        # Check that the response contains the login success message
        self.assertIn(b'You successfully logged in!', response.data)

    def test_logout(self):
        """Can a user logout?"""

        # Create a user
        user = User.signup(username='testuser', email='test@test.com', password='test123', image_url=None)
        db.session.commit()

        # Log in the user
        with self.client as c:
            with c.session_transaction() as session:
                session['user_id'] = user.id

            # Make a POST request to logout
            response = c.post('/logout', follow_redirects=True)

            # Check that the response contains the logout success message
            self.assertIn(b'You successfully logged out!', response.data)

            # Check that the user id is not in the session anymore
            self.assertNotIn('user_id', session)

# Run the tests
if __name__ == '__main__':
    unittest.main()
