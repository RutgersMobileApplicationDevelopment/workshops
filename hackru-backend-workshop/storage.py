

class BadDatabase():
    def __init__(self):
        pass

    def get_user(self, username):
        pass

    def load(self, file_name):
        pass

    def save(self, file_name=None):
        if self.file_name:
            pass
        pass

class User():
    # Never store passwords in plain text, like I have here!
    def __init__(self):
        pass

    def __load_from_username__(self, name):
        pass

    def login(self, password):
        pass

    def get_favorites(self):
        pass

    def add_favorite(self, meal_name):
        pass

    def rmv_favorite(self, meal_name):
        pass

