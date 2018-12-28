from app import db

class RepositoryBase(object):
    
    def __init__(self, item):
        self.item = item        

    def session(self):
        return db.session

    def create(self, item):        
        self.session().add(item)
        self.session().commit()

    def delete_by_id(self, id):
        deleted_item  = self.get_by_id(id)
        self.delete(deleted_item)
    
    def delete(self, item):
        self.session().delete(item)
        self.session().commit()

    def get_all(self):
        return self.item.query.all()

    def get_by_id(self, id):
        return self.item.query.filter_by(id=id).first()
