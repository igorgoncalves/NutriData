from domain.infraestructure.DbMongo import *

class RepositoryBase(object):
    """This class define a base method for all classes in repository layer"""
    def __init__(self, model_class):
        self.model_class  = model_class # specific which model class your son repo work's

    def get_all(self, **kwargs):
        """Lists all objects for the model_class in database."""
        return list(self.model_class.objects(**kwargs))

    def get_by_id(self, id):
        """Get a expecific object by your id."""
        return self.model_class.objects.with_id(object_id=id)

    def get_all_paginated(self, init=0, skip=10):
        """Lists all objects for the model_class in database."""
        return list(self.model_class.objects[init:(init+skip)])

    def create(self, object_instance):
        """Saves a model's instance in mongodb."""
        object_instance.save()
    
    def delete_by_id(self, id):
        """Deletes a object in mongodb by your id."""
        deleted_item  = self.get_by_id(id)
        self.delete(deleted_item)
    
    def delete(self, object_instance):
        """Deletes a object in mongodb by a existent instance."""
        self.model_class.delete(object_instance)
