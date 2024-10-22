from operator import attrgetter
class User:
    def __init__(self, u_id):
        self.u_id = u_id
    def __repr__(self) -> str:
        return f'User({self.u_id})'
users = [User(23), User(34), User(56), User(20)]
print(users)
print(sorted(users, key=attrgetter('u_id')))
print(sorted(users, key=lambda d: d.u_id))