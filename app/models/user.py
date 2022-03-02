# Model View Controller (MVC) - https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller


class User:
    def __init__(self, value):
        self.email = value.get("email")
        self.name = value.get("name")
        self.pk = value.get("pk")
        if not self.name:
            raise AttributeError("user name is required")

    @staticmethod
    def from_tuple(tup):
        # Note: these property assignments must be in the same order as the database columns in the UserDB class or the mappings will break
        return User(
            {
                "email": tup[0],
                "name": tup[1],
                "pk": tup[2],
            }
        )
