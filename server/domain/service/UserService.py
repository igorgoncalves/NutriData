from domain.models.User import User, UserSchema
from domain.repository.UserRepository import UserRepository
from domain.service._base import ServiceBase
from werkzeug.security import safe_str_cmp
from pprint import pprint


class UserService(ServiceBase):

    repository = UserRepository()
    schema = UserSchema()

    def __init__(self):
        super(UserService, self).__init__(repository=self.repository, schema=self.schema)


    @staticmethod
    def authenticate(username, password):
        repository = UserRepository()
        user = repository.get_all(username=username)
        if (len(user) > 0):
            user = user[0]

        if user and safe_str_cmp(user['password'].encode('utf-8'), password.encode('utf-8')):            
            user['id'] = str(user.id)
            return user
   
    @staticmethod
    def identity(payload):
        repository = UserRepository()
        user_id = payload['identity']
        return repository.get_by_id(user_id)

    @staticmethod
    def create_admin():
        repository = UserRepository()
        new_user = User(username="igorgoncalves", password="batata", email="igor_goncalves@live.com")
        repository.create(new_user)
