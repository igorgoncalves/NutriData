from domain.Database import *

class RepositoryBase(object):
    
    def __init__(self, item):
        self.item = item        

    def session(self):
        return session

    def create(self, item):        
        self.session().add(item)        

    def delete_by_id(self, id):
        deleted_item  = self.get_by_id(id)
        self.delete(deleted_item)
    
    def delete(self, item):
        self.session().delete(item)        

    def get_all(self):
        return self.session().query(self.item).all()

    def get_by_id(self, id):
        return self.session().query(self.item).filter_by(id=id).first()
    
    def save(self):
        self.session().commit()