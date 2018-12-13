from app.domain.repository._base import RepositoryBase

class ServiceBase(object):
    def __init__(self, repository=RepositoryBase):
        self.repository = repository

    def session(self):
        pass

    def create(self):
        return "oiori"

    def get_all(self):
        return self.repository.get_all(self.repository)
