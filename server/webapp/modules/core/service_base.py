from marshmallow import ValidationError


class ServiceBase(object):

    def __init__(self, model_class=None, schema=None):
        self.model_class = model_class
        self.schema = schema

    def get_all(self, **kwargs):
        """Lists all objects for the model_class in database."""
        return list(self.model_class.objects(**kwargs))

    def get_all_paginated(self, init, skip):
        """Lists all objects for the model_class in database."""
        return list(self.model_class.objects[init:(init+skip)])        

    def get_by_id(self, pk):
        """Get a expecific object by your id."""
        return self.model_class.objects.with_id(object_id=pk)

    def create(self, object_instance):
        """Saves a model's instance in mongodb."""
        item_saved = object_instance.save()
        return item_saved

    def createJson(self, json):
        item = self.deserialize(json)
        return self.create(item)

    def delete(self, object_instance):
        """Deletes a object in mongodb by a existent instance."""
        self.model_class.delete(object_instance)
        
    def delete_by_id(self, pk):
        """Deletes a object in mongodb by your id."""
        deleted_item = self.get_by_id(pk)
        self.delete(deleted_item)

    def update(self, object_instance):
        """Deletes a object in mongodb by a existent instance."""
        return object_instance.save()

    def deserialize(self, json):
        item, err = self.schema.load(json)
        return item

    def serialize(self, item, many=False):
        json = self.schema.dumps(item, many)
        return json

    def validate(self, item_dict):
        try:
            self.schema.load(item_dict)
            return {}, True
        except ValidationError as err:
            error = err
            return {'detail': error}, False
