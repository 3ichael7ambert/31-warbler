from unittest import TestCase
from models import db, User, Message
from app import app

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# Use test database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///warbler-test'

# Disable CSRF tokens in the forms (only for testing purposes!)
app.config['WTF_CSRF_ENABLED'] = False

class MessageModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        user = User.signup(username='testuser', email='test@test.com', password='test123', image_url=None)
        db.session.commit()

        self.user = user
        self.client = app.test_client()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_message_model(self):
        """Does the basic message model work?"""

        message = Message(text='Test message', user_id=self.user.id)
        db.session.add(message)
        db.session.commit()

        # Check that the message was successfully created
        self.assertEqual(message.text, 'Test message')
        self.assertEqual(message.user_id, self.user.id)

        # Check that the message is associated with the correct user
        self.assertEqual(message.user, self.user)

        # Check that the message is added to the user's messages
        self.assertIn(message, self.user.messages.all())

def test_message_repr(self):
    message = Message(text="Test message", user_id=1)
    db.session.add(message)
    db.session.commit()
    expected_repr = "<Message #1: Test message, User ID: 1>"
    self.assertEqual(repr(message), expected_repr)


# Run the tests
if __name__ == '__main__':
    unittest.main()
