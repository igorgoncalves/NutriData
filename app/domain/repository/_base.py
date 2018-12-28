from app import db

class RepositoryBase(object):
    def __init__(self, item):
        self.item = item
        print(str(item))

    def session(self):
        return db.session

    def create(self, item):        
        self.session().add(item)
        self.session().commit()

    def remove_by_id(self, id):
        pass

    def get_all(self):
        return self.item.query.all()

    def get_by_id(self, id):
        return self.item.query.filter_by(id=id).first()
