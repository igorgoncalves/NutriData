from werkzeug.security import safe_str_cmp

from webapp.modules.core.service_base import ServiceBase

from .models import User
from .schemas import UserSchema


class UserService(ServiceBase):

    schema = UserSchema()
    repository = ServiceBase(model_class=User, schema=schema)

    def __init__(self):
        super(UserService, self).__init__(
            model_class=User, schema=self.schema)

    @staticmethod
    def authenticate(username, password):
        schema = UserSchema()
        repository = ServiceBase(model_class=User, schema=schema)
        user = repository.get_all(username=username)
        if (len(user) > 0):
            user = user[0]

        if user and safe_str_cmp(user['password'].encode('utf-8'), password.encode('utf-8')):
            user['id'] = str(user.id)
            return user

    @staticmethod
    def identity(payload):
        schema = UserSchema()
        repository = ServiceBase(model_class=User, schema=schema)
        user_id = payload['identity']
        return repository.get_by_id(user_id)

    @staticmethod
    def create_user(username, password, email):
        schema = UserSchema()
        repository = ServiceBase(model_class=User, schema=schema)
        new_user = User(username=username, password=password, email=email)
        repository.create(new_user)
