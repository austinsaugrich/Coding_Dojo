from app.config.mysqlconnection import MySQLConnection


class User:
    def __init__(self, data,):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']

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
            all_users.append(User(row,))
        return all_users

    @classmethod
    def delete(cls, id):
        query = """
        DELETE FROM users WHERE users.id = %(id)s
        """
        return MySQLConnection('users').query_db(query, {'id': id})

    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT * from users WHERE users.id = %(id)s;'

        results = MySQLConnection('users').query_db(query, {'id': id})

        return User(results[0])

    @classmethod
    def edit(cls, data,):
        query = """
        UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
WHERE users.id = %(id)s
        """
        return MySQLConnection('users').query_db(query, data)
