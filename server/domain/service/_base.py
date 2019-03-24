from domain.repository._base import RepositoryBase

class ServiceBase(object):

    def __init__(self, repository=RepositoryBase, schema=None):
        self.repository = repository
        self.schema = schema

    def get_all(self, **kwargs):
        return self.repository.get_all(**kwargs)
    
    def get_all_paginated(self, init, skip):
        return self.repository.get_all_paginated(init, skip)
    
    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def create(self, item):
        return self.repository.create(item)

    def createJson(self, json):
        item = self.deserialize(json)
        self.create(item)

    def delete(self, item):
        self.repository.delete(item)

    def delete_by_id(self, id):
        self.repository.delete_by_id(id)

    def deserialize(self, json):
        item, err = self.schema.load(json)
        return item

    def serialize(self, item, many=False):
        json = self.schema.dumps(item, many)
        return json
