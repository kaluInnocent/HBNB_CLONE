#!/usr/bin/python3
"""modules for time and uuid"""

import uuid
from datetime import datetime
#import models

class BaseModels:
    """a class BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self):
        """A constructor that instantiates a new object"""
        self.id = str(iuuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)
    
    def __str__(self):
        """Method prints the string representation of the Basemodel class
        """  
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Method updates the the date date of creation 
        """
        self.updated_at = datetime.now()
        #models.storage.save()
    
    def to_dict(self):
        """Method returns a dictionary containing all keys/values
        of __dict__
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic