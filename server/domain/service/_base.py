from server.domain.repository._base import RepositoryBase
from marshmallow import ValidationError


class ServiceBase(object):

    def __init__(self, repository: RepositoryBase, schema=None):
        self.repository = repository
        self.schema = schema

    def get_all(self, **kwargs):
        return self.repository.get_all(**kwargs)
    
    def get_all_paginated(self, init, skip):
        return self.repository.get_all_paginated(init, skip)
    
    def get_by_id(self, pk):
        return self.repository.get_by_id(pk)

    def create(self, item):        
        self.repository.create(item)            
        return item

    def createJson(self, json):
        item = self.deserialize(json)
        return self.create(item)

    def delete(self, item):
        return self.repository.delete(item)

    def delete_by_id(self, pk):
        self.repository.delete_by_id(pk)

    def update(self, item):
        return self.repository.update(item)

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
            return { 'detail': error }, False