from marshmallow_mongoengine import ModelSchema
from .models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
