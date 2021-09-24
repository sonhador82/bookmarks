from marshmallow import Schema, fields, post_load


class Bookmark:
    def __init__(self, title, url, description, category, tags, _id=None):
        self._id = _id
        self.title = title
        self.url = url
        self.description = description
        self.category = category
        self.tags = tags

    def __repr__(self):
        return f'<Bookmark id={self._id} title={self.title} >'


class BookmarkSchema(Schema):
    _id = fields.Raw(load_only=True)
    title = fields.Str()
    url = fields.URL()
    description = fields.Str()
    category = fields.Str()
    tags = fields.List(fields.Str())

    @post_load
    def make_user(self, data, **kwargs):
        return Bookmark(**data)
