from marshmallow import Schema, fields, post_load, pre_load


class Bookmark:
    def __init__(self, user_id, title, url, description, category, tags, _id=None):
        self._id = _id
        self.title = title
        self.url = url
        self.description = description
        self.category = category
        self.tags = tags
        self.user_id = user_id

    def __repr__(self):
        return f'<Bookmark id={self._id} title={self.title} >'

    def __eq__(self, other):
        return self._id == other._id


class BookmarkSchema(Schema):
    _id = fields.Str(load_only=True)
    title = fields.Str()
    url = fields.URL()
    description = fields.Str()
    category = fields.Str()
    tags = fields.List(fields.Str())
    user_id = fields.Str()

    @pre_load
    def convert_object_id(self, in_data, **kwargs):
        in_data['_id'] = str(in_data['_id'])
        return in_data

    @post_load
    def make_bookmark(self, data, **kwargs):
        return Bookmark(**data)
