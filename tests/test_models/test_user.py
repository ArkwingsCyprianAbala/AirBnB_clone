import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        creates a temporary testfile for saving data
        """
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        Removes the temporary test file after save
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        """
        Create a new User instance
        Check if the default email attribute is an empty string
        Check if the default first_name attribute is an empty string
        Check if the default last_name attribute is an empty string
        """
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def test_user_inherit_from_base_model(self):
        """
        Create a user interface
        Check if the User class is a subclass of BaseModel
        """
        test_user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        """
        Check if user is present in the string representation
        """
        test_user = User()
        test_user.email = "cyprian@example.com"
        test_user.first_name = "Cyprian"
        test_user.last_name = "Abala"
        test_user.password = "password123"
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("cyprian@example.com", user_str)
        self.assertIn("Cyprian", user_str)
        self.assertIn("Abala", user_str)

    def test_user_to_dict(self):
        """
        Check if the user instances match the set values
        """
        test_user = User()
        test_user.email = "cyprian@example.com"
        test_user.first_name = "Cyprian"
        test_user.last_name = "Abala"
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "cyprian@example.com")
        self.assertEqual(user_dict['first_name'], "Cyprian")
        self.assertEqual(user_dict['last_name'], "Abala")

    def test_user_id_generation(self):
        """
        Ensure that the 'id' attribute of each User instance is unique
        """
        test_user = User()
        user2 = User()
        self.assertNotEqual(test_user.id, user2.id)


if __name__ == '__main__':
    unittest.main()
