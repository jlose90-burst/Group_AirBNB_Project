from lib.User import User

class UserRepository:
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users ORDER BY id ASC")
        users = []
        for row in rows:
            item = User(row['username'],row['password'],row['email'],row['phone'], row['id'])
            users.append(item)
        return users
    
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        if not rows:
            return None
        row = rows[0]
        return User(row['username'],row['password'],row['email'],row['phone'], row['id'])

    def find_by_username(self, username):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s', [username])
        if not rows:
            return None
        row = rows[0]
        return User(row['username'],row['password'],row['email'],row['phone'], row['id'])

    def find_by_email(self, email):
        rows = self._connection.execute(
            'SELECT * from users WHERE email = %s', [email])
        if not rows:
            return None
        row = rows[0]
        return User(row['username'],row['password'],row['email'],row['phone'], row['id'])
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (username,password,email,phone) VALUES (%s, %s, %s, %s)', [
                                    user.username, user.password, user.email, user.phone])
        return None

    def return_user_email(self,user_id):
        self._connection.execute(
            'SELECT email from users WHERE id = %s', [user_id])
        return None