import hashlib
from json import JSONEncoder


class User:
    def __init__(self, email: str, full_name: str, password: str, is_admin: bool = False):
        self.email = email
        self.full_name = full_name
        self.password = password
        self.is_admin = is_admin

    def __eq__(self, other: 'User'):
        cur_md5 = hashlib.md5(f'{self.email}{self.password}'.encode('utf-8')).hexdigest()
        other_md5 = hashlib.md5(f'{other.email}{other.password}'.encode('utf-8')).hexdigest()
        return cur_md5 == other_md5

    def __repr__(self):
        return f'<User email={self.email} >'


class UserJsonEncoder(JSONEncoder):
    def default(self, o):
        try:
            json_data = o.__dict__
        except TypeError:
            pass
        else:
            return json_data
        # Let the base class default method raise the TypeError
        return JSONEncoder.default(self, o)


async def check_credentials(storage, email, password):
    u = await storage.find_user_by_email(email)
    return u.password == password
