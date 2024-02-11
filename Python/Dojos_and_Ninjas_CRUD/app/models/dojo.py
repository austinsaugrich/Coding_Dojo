
from app.config.mysqlconnection import MySQLConnection
from app.models import ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return MySQLConnection('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s'
        results = MySQLConnection(
            'dojos_and_ninjas_schema').query_db(query, {'id': data})
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                'id': row_from_db["ninjas.id"],
                'first_name': row_from_db["first_name"],
                'last_name': row_from_db["last_name"],
                'age': row_from_db["age"],
                'created_at': row_from_db["ninjas.created_at"],
                'updated_at': row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos(name) VALUES(%(name)s)'
        return MySQLConnection('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT * FROM dojos WHERE dojos.id = %(id)s'
        results = MySQLConnection(
            'dojos_and_ninjas_schema').query_db(query, {'id': id})
        return Dojo(results[0])

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos'
        results = MySQLConnection('dojos_and_ninjas_schema').query_db(query)
        all_dojos = []
        for row in results:
            all_dojos.append(Dojo(row).__dict__)
        return all_dojos
