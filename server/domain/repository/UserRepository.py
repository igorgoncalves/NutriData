from server.domain.models.User import User
from server.domain.repository._base import RepositoryBase


class UserRepository(RepositoryBase):
    def __init__(self):
        """Specificy for the father class which model class this repo works."""
        super(UserRepository, self).__init__(model_class=User)