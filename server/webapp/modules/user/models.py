from mongoengine import Document, StringField, EmailField


class User(Document):
    username = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)

    def __repr__(self):
        return '<Usuer(ano={self.username!r}>'.format(self=self)
