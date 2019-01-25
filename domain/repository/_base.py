from domain.infraestructure import DbMongo

class RepositoryBase(object):
    
    def __init__(self, item):
        self.item = item        

    def create(self, object_instance):        
        object_instance.save()

    def delete_by_id(self, id):
        deleted_item  = self.get_by_id(id)
        self.delete(deleted_item)
    
    def delete(self, item):
        self.item.delete(item)        

    def get_all(self):
        return list(self.item.objects)

    def get_by_id(self, id):
        return self.item.objects.with_id(object_id=id) 
    
    def save(self):
        # self.session().commit()
        pass