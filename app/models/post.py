
class Post:
    def __init__(self, value):
        self.content = value.get("content")
        self.title = value.get("title")
        self.insertedAt = value.get("insertedAt")
        self.modifiedAt = value.get("modifiedAt")
        self.userPk = value.get("userPk")
        self.pk = value.get("pk")
        if not self.content:
            raise AttributeError("Post content is required")

    @staticmethod
    def from_tuple(tup):
        # Note: these property assignments must be in the same order as the database columns in the PostDB class or the mappings will break
        return Post(
            {
                "content": tup[0],
                "title": tup[1],
                "insertedAt": tup[2],
                "modifiedAt": tup[3],
                "userPk": tup[4],
                "pk": tup[5],
            }
        )
