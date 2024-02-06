from app.config.mysqlconnection import MySQLConnection


class User:
    def __init__(self, data, created_at=0):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = created_at

    @classmethod
    def add(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email)
VALUES(%(first_name)s, %(last_name)s, %(email)s);
        """

        return MySQLConnection('users').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'

        results = MySQLConnection('users').query_db(query)

        all_users = []
        for row in results:
            all_users.append(User(row, row['created_at']))
        return all_users
