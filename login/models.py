from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,id):
        self.id = id
        self.name = "user" + str(id)
        self.pwd = self.name + "_password"

    def __repr__(self):
        return "%d/%s/%s" %(self.id,self.name,self.pwd)

