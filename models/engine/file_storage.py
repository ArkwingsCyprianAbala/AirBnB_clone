#!/usr/bin/python3
"""

"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """

    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """

        :param obj:
        :return:
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """

        :return:
        """
        return FileStorage.__objects

    def save(self):
        """
        This serializes the __objects dictionary into JSON format and saves it to the file specified by __file_path
        """
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """

        :param self:
        :return:
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, values in obj_dict.item():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
