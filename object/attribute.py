# Define attribute with name
class attribute:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return str(self.name)

    def set_name(self, name):
        self.name = name