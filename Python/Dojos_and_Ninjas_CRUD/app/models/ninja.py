from app.config.mysqlconnection import MySQLConnection


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_ninja(cls, data):
        query = 'INSERT INTO ninjas(first_name, last_name, age, dojos_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)'
        return MySQLConnection('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_all(cls, id):
        query = 'SELECT * FROM ninjas WHERE dojos_id = %(id)s'
        results = MySQLConnection(
            'dojos_and_ninjas_schema').query_db(query, {'id': id})
        all_ninjas = []
        for row in results:
            all_ninjas.append(Ninja(row).__dict__)
        return all_ninjas
