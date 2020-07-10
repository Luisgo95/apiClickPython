import uuid


class Client:
    def __init__(self,name,company,email,positio, Uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid= uid or uuid.uuid4()
    
    
    def to_dict(self):
        #representación diccionario de nuestro objeto
        return vars(self)
    @staticmethod
    def schema():
        return['name','company','email','position','uid']

        