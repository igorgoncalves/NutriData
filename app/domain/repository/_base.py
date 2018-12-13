from injector import inject

class RepositoryBase(object):
    @inject
    def __init__(self, db):
        pass

    def session(self):
        pass

    def create(item):
        pass

    def remove_by_id(self, id):
        pass

    def get_all():
        pass

    def get_by_id(id):
        return str(id)
