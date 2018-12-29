from domain.repository._base import RepositoryBase

class ServiceBase(object):

    def __init__(self, repository=RepositoryBase):        
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()
    
    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def create(self, item):
        self.repository.create(item)
        self.repository.save()
    
    def delete(self, item):
        self.repository.delete(item)
        self.repository.save()
    
    def delete_by_id(self, id):
        self.repository.delete_by_id(id)