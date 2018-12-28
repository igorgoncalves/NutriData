from app.domain.repository._base import RepositoryBase

class ServiceBase(object):
    def __init__(self, repository=RepositoryBase):        
        self.repository = repository

    def create(self, item):
        return self.repository.create(item)

    def get_all(self):
        return self.repository.get_all()
    
    def get_by_id(self, id):
        return self.repository.get_by_id(id)