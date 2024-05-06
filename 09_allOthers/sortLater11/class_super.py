from datetime import datetime

class Animal23(object):
    def __init__(self, species23):
        super(Animal23, self).__init__()
        self.species23 = species23
        self.createdAt = datetime.now()


objInstance11 = Animal23('cat')
print("objInstance11 class ===> ", objInstance11)
print("objInstance11 properties ===> ", objInstance11.species23, objInstance11.createdAt)