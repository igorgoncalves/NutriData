from injector import inject

class RepositoryBase(object):
    def __init__(self, db, item):
        self.db = db
        self.item = item
        print(str(item))

    def session(self):
        pass

    def create(item):
        pass

    def remove_by_id(self, id):
        pass

    def get_all(self):
        return self.item.query.all()

    def get_by_id(self, id):
        return str(id)
