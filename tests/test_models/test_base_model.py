#!/usr/bin/python3
"""

"""

import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    def test_init(self):
        """
        Check to see that all the attributes have values when an instance of a Base class is created.
        """
        mine_model = BaseModel()

        self.assertIsNotNone(mine_model.id)
        self.assertIsNotNone(mine_model.created_at)
        self.assertIsNotNone(mine_model.updated_at)

    def test_save(self):
        """
        Check to see that the initial update time and the current update time are not equal.
        """
        mine_model = BaseModel()

        initial_update = mine_model.updated_at
        current_update = mine_model.save()
        self.assertNotEqual(initial_update, current_update)

    def test_to_dict(self):
        """
        Checks to see if to_dict method is working as expected.
        """
        mine_model = BaseModel()

        mine_model_dict = mine_model.to_dict()

        self.assertIsInstance(mine_model_dict, dict)

        self.assertEqual(mine_model_dict["__class__"], 'BaseModel')
        self.assertEqual(mine_model_dict['id'], mine_model.id)
        self.assertEqual(mine_model_dict['created_at'], mine_model.created_at.isoformat())
        self.assertEqual(mine_model_dict['updated_at'], mine_model.updated_at.isoformat())

    def test_str(self):
        """
        Check on the string representation of new instance created.
        """
        mine_model = BaseModel()

        self.assertTrue(str(mine_model).startswith('[BaseModel]'))
        self.assertIn(mine_model.id, str(mine_model))
        self.assertIn(str(mine_model.__dict__), str(mine_model))


if __name__ == '__main__':
    unittest.main()
